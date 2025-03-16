#!/usr/bin/env python3

import click
from tabulate import tabulate as t
from desco import DescoPrepaid

@click.group()
def app():
    pass

@app.command(help="Get balance and consumption")
@click.option('--accountid', '-a', type=click.INT, required=True, help="Account ID")
def get_balance(accountid):
    data = DescoPrepaid(accountid).get_balance()
    print(t(data))

@app.command(help="Get customer info")
@click.option('--accountid', '-a', type=click.INT, required=True, help="Account ID")
def get_customer_info(accountid):
    data = DescoPrepaid(accountid).get_customer_info()
    print(t(data))

@app.command(help="Get recharge history")
@click.option('--accountid', '-a', type=click.INT, required=True, help="Account ID")
def get_recharge_history(accountid):
    data, headers = DescoPrepaid(accountid).get_recharge_history()
    print(t(data, headers=headers))

@app.command(help="Get monthly consumption")
@click.option('--accountid', '-a', type=click.INT, required=True, help="Account ID")
def get_monthly_consumption(accountid):
    data, headers = DescoPrepaid(accountid).get_monthly_consumption()
    print(t(data, headers=headers))

if __name__ == "__main__":
    app()