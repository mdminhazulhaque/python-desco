#!/usr/bin/env python3

__author__ = "Md. Minhazul Haque"
__version__ = "0.0.1"
__license__ = "GPLv3"

"""
Copyright (c) 2022 Md. Minhazul Haque
This file is part of mdminhazulhaque/desco-prepaid-cli
(see https://github.com/mdminhazulhaque/desco-prepaid-cli).
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

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
