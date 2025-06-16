#!/usr/bin/env python3
"""
Desco Prepaid CLI

A command-line interface for interacting with DESCO prepaid electricity accounts.
Provides commands to check balance, get customer info, view consumption history,
and track recharge records.
"""

import click
import sys
from tabulate import tabulate
from .desco import DescoPrepaid


def handle_api_error(func):
    """Decorator to handle API errors gracefully."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            click.echo(f"❌ Error: {str(e)}", err=True)
            sys.exit(1)
    return wrapper


@click.group()
@click.version_option(version="0.1.0", prog_name="desco-cli")
def app():
    """
    🔌 Desco Prepaid CLI
    
    A command-line tool for managing DESCO prepaid electricity accounts.
    Get real-time balance, consumption data, customer information, and recharge history.
    """
    pass


@app.command(name="get-balance")
@click.option(
    '--accountid', '-a', 
    type=click.STRING, 
    required=True, 
    help="DESCO prepaid account number"
)
@handle_api_error
def get_balance(accountid):
    """Get current account balance and consumption information."""
    click.echo("💰 Fetching account balance...")
    
    client = DescoPrepaid(accountid)
    data = client.get_balance()
    
    if data:
        click.echo("\n📊 Account Balance & Consumption:")
        click.echo(tabulate(data, tablefmt="simple"))
    else:
        click.echo("⚠️  No balance data found for this account.")


@app.command(name="get-customer-info")
@click.option(
    '--accountid', '-a', 
    type=click.STRING, 
    required=True, 
    help="DESCO prepaid account number"
)
@handle_api_error
def get_customer_info(accountid):
    """Get detailed customer and meter information."""
    click.echo("👤 Fetching customer information...")
    
    client = DescoPrepaid(accountid)
    data = client.get_customer_info()
    
    if data:
        click.echo("\n📋 Customer Information:")
        click.echo(tabulate(data, tablefmt="simple"))
    else:
        click.echo("⚠️  No customer data found for this account.")


@app.command(name="get-recharge-history")
@click.option(
    '--accountid', '-a', 
    type=click.STRING, 
    required=True, 
    help="DESCO prepaid account number"
)
@handle_api_error
def get_recharge_history(accountid):
    """Get recharge and payment history for the account."""
    click.echo("🔄 Fetching recharge history...")
    
    client = DescoPrepaid(accountid)
    data, headers = client.get_recharge_history()
    
    if data:
        click.echo("\n💳 Recharge History:")
        click.echo(tabulate(data, headers=headers, tablefmt="simple"))
    else:
        click.echo("⚠️  No recharge history found for this account.")


@app.command(name="get-monthly-consumption")
@click.option(
    '--accountid', '-a', 
    type=click.STRING, 
    required=True, 
    help="DESCO prepaid account number"
)
@handle_api_error
def get_monthly_consumption(accountid):
    """Get monthly consumption history for the account."""
    click.echo("📊 Fetching monthly consumption data...")
    
    client = DescoPrepaid(accountid)
    data, headers = client.get_monthly_consumption()
    
    if data:
        click.echo("\n⚡ Monthly Consumption History:")
        click.echo(tabulate(data, headers=headers, tablefmt="simple"))
    else:
        click.echo("⚠️  No consumption data found for this account.")


if __name__ == "__main__":
    app()
