#!/usr/bin/env python3
"""
Desco Prepaid CLI

Command-line interface for DESCO prepaid electricity accounts. The core
`DescoPrepaid` engine returns plain dicts; this CLI renders them as tables.
"""

import sys
import functools

import click
import requests
from tabulate import tabulate

from .desco import DescoPrepaid
from . import __version__


def handle_api_error(func):
    """Decorator to handle API errors gracefully."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            click.echo(
                f"❌ Could not reach the DESCO API.\n"
                "   The service may be down or temporarily unreachable from your network. "
                "Please try again later.",
                err=True,
            )
            sys.exit(1)
        except Exception as e:
            click.echo(f"❌ Error: {str(e)}", err=True)
            sys.exit(1)
    return wrapper


def _kv_table(data: dict):
    return [[k, "" if v is None else v] for k, v in data.items()]


@click.group()
@click.version_option(version=__version__, prog_name="desco-cli")
def app():
    """
    🔌 Desco Prepaid CLI

    A command-line tool for managing DESCO prepaid electricity accounts.
    Get real-time balance, consumption data, customer information, and recharge history.
    """
    pass


@app.command(name="get-balance")
@click.option("--accountid", "-a", type=click.STRING, required=True, help="DESCO prepaid account number")
@handle_api_error
def get_balance(accountid):
    """Get current account balance and consumption information."""
    click.echo("💰 Fetching account balance...")
    data = DescoPrepaid(accountid).get_balance()
    if data:
        click.echo("\n📊 Account Balance & Consumption:")
        click.echo(tabulate(_kv_table(data), tablefmt="simple"))
    else:
        click.echo("⚠️  No balance data found for this account.")


@app.command(name="get-customer-info")
@click.option("--accountid", "-a", type=click.STRING, required=True, help="DESCO prepaid account number")
@handle_api_error
def get_customer_info(accountid):
    """Get detailed customer and meter information."""
    click.echo("👤 Fetching customer information...")
    data = DescoPrepaid(accountid).get_customer_info()
    if data:
        click.echo("\n📋 Customer Information:")
        click.echo(tabulate(_kv_table(data), tablefmt="simple"))
    else:
        click.echo("⚠️  No customer data found for this account.")


@app.command(name="get-recharge-history")
@click.option("--accountid", "-a", type=click.STRING, required=True, help="DESCO prepaid account number")
@handle_api_error
def get_recharge_history(accountid):
    """Get recharge and payment history for the account."""
    click.echo("🔄 Fetching recharge history...")
    data = DescoPrepaid(accountid).get_recharge_history()
    if data:
        click.echo("\n💳 Recharge History:")
        click.echo(tabulate(data, headers="keys", tablefmt="simple"))
    else:
        click.echo("⚠️  No recharge history found for this account.")


@app.command(name="get-monthly-consumption")
@click.option("--accountid", "-a", type=click.STRING, required=True, help="DESCO prepaid account number")
@handle_api_error
def get_monthly_consumption(accountid):
    """Get monthly consumption history for the account."""
    click.echo("📊 Fetching monthly consumption data...")
    data = DescoPrepaid(accountid).get_monthly_consumption()
    if data:
        click.echo("\n⚡ Monthly Consumption History:")
        click.echo(tabulate(data, headers="keys", tablefmt="simple"))
    else:
        click.echo("⚠️  No consumption data found for this account.")


if __name__ == "__main__":
    app()
