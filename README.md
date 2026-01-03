# 🔌 Desco Prepaid CLI

[![PyPI version](https://badge.fury.io/py/desco.svg)](https://badge.fury.io/py/desco)
[![Python Versions](https://img.shields.io/pypi/pyversions/desco.svg)](https://pypi.org/project/desco/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/desco)](https://pepy.tech/project/desco)

A Python CLI tool to collect information about **Dhaka Electric Supply Company Limited (DESCO)** prepaid electricity accounts. Get real-time balance, consumption data, customer information, and recharge history directly from your terminal.

## ✨ Features

- 💰 **Balance Check**: Get current balance and monthly consumption
- 👤 **Customer Info**: Retrieve detailed customer and meter information  
- 📊 **Monthly Consumption**: View historical monthly usage data
- 🔄 **Recharge History**: Track your payment and recharge records
- 🚀 **Fast & Lightweight**: Built with Python and designed for speed
- 🔒 **Secure**: Direct API integration with DESCO's official endpoints

## 📦 Installation

### From PyPI (Recommended)
```bash
pip install desco
```

### From Source
```bash
git clone https://github.com/mdminhazulhaque/python-desco.git
cd python-desco
pip install -e .
```

## 🚀 Quick Start

After installation, use the `desco-cli` command:

```bash
# Get help
desco-cli --help

# Check balance
desco-cli get-balance -a YOUR_ACCOUNT_NUMBER

# Get customer information
desco-cli get-customer-info -a YOUR_ACCOUNT_NUMBER
```

## 📖 Usage

```
Usage: desco-cli [OPTIONS] COMMAND [ARGS]...

  A CLI tool for Desco Prepaid electricity account management.

Options:
  --help  Show this message and exit.

Commands:
  get-balance              Get current balance and consumption data
  get-customer-info        Get detailed customer and meter information
  get-monthly-consumption  Get monthly consumption history
  get-recharge-history     Get recharge and payment history
```

## 💡 Examples

### 💰 Check Balance

Get your current account balance and this month's consumption:

```bash
$ desco-cli get-balance -a 987654321
```

**Sample Output:**
```
-----------------------  -------------------
accountNo                987654321
meterNo                  667788990011
balance                  1384.35
currentMonthConsumption  2020.49
readingTime              2022-07-19 00:00:00
-----------------------  -------------------
```

### 👤 Get Customer Information

Retrieve comprehensive customer and meter details:

```bash
$ desco-cli get-customer-info -a 987654321
```

**Sample Output:**
```
-------------------  --------------------------
accountNo            987654321
contactNo            01833000000
customerName         MR. JOHN DOE
feederName           Sector 11
installationAddress  H-42, R-7, SEC-13, UTTARA
installationDate     2019-06-23 00:00:00
meterNo              667788990011
phaseType            Single Phase Meter
registerDate         2019-06-23 00:00:00
sanctionLoad         6
tariffSolution       Category-A: Residential
meterModel           None
transformer          None
SDName               Turag
-------------------  --------------------------
```

### 🔄 Get Recharge History

View your recent payment and recharge transactions:

```bash
$ desco-cli get-recharge-history -a 987654321
```

**Sample Output:**
```
rechargeDate           totalAmount     vat    energyAmount
-------------------  -------------  ------  --------------
2022-07-14 06:59:49           2000   95.24         1923.81
2022-07-09 16:35:34           1000   47.62          521.1
2022-05-30 19:31:52           3000  142.86         2665.31
2022-04-21 10:57:38           1980   94.29         1904.57
2022-04-08 23:29:45           1000   47.62          741.5
2022-03-31 10:02:25            500   23.81          480.95
2022-03-01 13:33:16           2000   95.24         1703.41
2022-02-22 12:25:31           2970  141.43          432.46
```

### 📊 Get Monthly Consumption

Analyze your monthly electricity usage patterns:

```bash
$ desco-cli get-monthly-consumption -a 987654321
```

**Sample Output:**
```
month      consumedTaka    consumedUnit    maximumDemand
-------  --------------  --------------  ---------------
2022-01            9              2.401            0
2022-02          162.45          43.323            2.08
2022-03         2204.92         390.8              2.69
2022-04         1260.25         238.501            2.924
2022-05         1292.47         243.864            3.764
2022-06         2222.68         393.6              3.57
2022-07         3901.46         564.81             2.546
2022-08         2891.26         463.185            3.302
2022-09         2032.6          363.622            2.69
2022-10          735.81         148.695            1.8
2022-11         1223.71         232.408            3.486
```

## 🛠️ Development

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Setting up for Development

1. Clone the repository:
```bash
git clone https://github.com/mdminhazulhaque/python-desco.git
cd python-desco
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e .
```

### Dependencies

- `requests` - HTTP library for API calls
- `click` - Command line interface framework
- `tabulate` - Pretty-print tabular data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This is an unofficial tool. Use at your own discretion. The authors are not responsible for any issues that may arise from using this tool.