# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python CLI tool for interacting with Dhaka Electric Supply Company Limited (DESCO) prepaid electricity account APIs. It provides read-only access to balance, customer information, monthly consumption, and recharge history through a command-line interface.

## Architecture

### Core Components

**desco/desco.py** - API Client Layer
- `DescoPrepaid` class handles all HTTP communication with DESCO endpoints
- Base URL: `https://prepaid.desco.org.bd/api/tkdes/customer`
- **No authentication required** - only account number needed
- SSL verification disabled with `verify=False` due to DESCO's certificate issues
- urllib3 warnings suppressed via `urllib3.disable_warnings()`
- Type hints throughout using `typing` module
- Methods return tuple of `(data, headers)` or `List[List[str]]`

**desco/main.py** - CLI Layer
- Click-based CLI using decorator pattern (`@app.command(name="...")`)
- Commands use `--accountid` / `-a` option (STRING type, not INT)
- Error handling through `handle_api_error` decorator wrapper
- Entry point: `app()` function mapped to `desco-cli` in pyproject.toml
- Uses tabulate for formatted output display

**desco/__init__.py** - Package Entry Point
- Exports `DescoPrepaid` class for programmatic use
- Version controlled by GitHub Actions during release (format: `1.{run_number}.0`)

### API Design Pattern

All API methods follow this pattern:
1. Build params dict with `accountNo` as base
2. Add method-specific params (date ranges for history queries)
3. Call `_make_request(endpoint, params)` helper
4. Parse JSON response from `response['data']`
5. Return formatted data structure

### Date Range Handling

Historical data methods (`get_recharge_history`, `get_monthly_consumption`) use:
- `DEFAULT_HISTORY_DAYS = 335` (~11 months)
- Auto-calculate `dateFrom` and `dateTo` using `datetime` and `timedelta`
- Date format: `"%Y-%m-%d"` for recharge, `"%Y-%m"` for monthly consumption

### API Endpoints

```python
ENDPOINTS = {
    'customer_info': '/getCustomerInfo',
    'balance': '/getBalance',
    'monthly_consumption': '/getCustomerMonthlyConsumption',
    'recharge_history': '/getRechargeHistory'
}
```

## Development Commands

### Setup
```bash
# Install in development mode
pip install -e .

# Or create virtual environment first
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
```

### Testing the CLI
```bash
# Test balance check
desco-cli get-balance -a 987654321

# Test customer info
desco-cli get-customer-info -a 987654321

# Test recharge history
desco-cli get-recharge-history -a 987654321

# Test monthly consumption
desco-cli get-monthly-consumption -a 987654321
```

### Building
```bash
# Build distribution packages
python -m pip install build
python -m build

# Output: dist/*.whl and dist/*.tar.gz
```

## Version Management

- Version is defined in `desco/__init__.py` as `__version__ = "1.0.0"`
- GitHub Actions workflow (`.github/workflows/pypi.yml`) auto-updates version on push to main
- Version format: `1.{github.run_number}.0`
- Workflow uses sed to replace version string: `sed -i "s/__version__ = \".*\"/__version__ = \"$VERSION\"/" desco/__init__.py`

## Publishing

Automated via GitHub Actions on push to main:
1. Version number updated automatically
2. Build artifacts created with `python -m build`
3. Published to PyPI using trusted publisher with OIDC token

Manual workflow dispatch also available via GitHub Actions UI.

## API Response Structures

### Balance Response
Returns `List[List[str]]` of `[key, value]` pairs from `response['data']`:
- accountNo, meterNo, balance, currentMonthConsumption, readingTime

### Customer Info Response
Returns `List[List[str]]` of `[key, value]` pairs from `response['data']`:
- accountNo, contactNo, customerName, feederName, installationAddress
- installationDate, meterNo, phaseType, registerDate, sanctionLoad
- tariffSolution, meterModel, transformer, SDName

### Recharge History Response
Returns tuple `(data, headers)`:
- Headers: `['rechargeDate', 'totalAmount', 'vat', 'energyAmount']`
- Data extracted from `response['data']` array, mapping `VAT` (uppercase) to vat

### Monthly Consumption Response
Returns tuple `(data, headers)`:
- Headers: `['month', 'consumedTaka', 'consumedUnit', 'maximumDemand']`
- Data extracted from `response['data']` array

## CLI Design Pattern

Commands using `@app.command(name="...")` decorator pattern (different from bpdb's `app.add_command()` pattern):
1. Click decorator defines command with `--accountid` option
2. `@handle_api_error` decorator catches exceptions and exits with error code 1
3. Print status message with emoji
4. Instantiate `DescoPrepaid(accountid)`
5. Call API method
6. Format output with tabulate

## Important Notes

- This is part of a multi-repository project with sibling repositories: `python-bpdb` and `python-nesco` (similar utility tools for other Bangladesh power companies)
- All three repositories share similar CLI structure but different API integration patterns
- **No authentication or token storage** - simpler than bpdb
- SSL verification disabled - DESCO's certificate has issues
- API uses HTTPS but with `verify=False`
- Type hints included for better IDE support
- Dependencies include `urllib3` explicitly (not in other projects)
- Account ID treated as STRING in CLI (not INT like nesco)
