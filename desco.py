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

import requests
from datetime import timedelta, datetime

class DescoPrepaid(object):
    
    URL_BASE = 'https://prepaid.desco.org.bd/api/tkdes/customer'
    URL_CUSTOMER_INFO = '/getCustomerInfo'
    URL_BALANCE = '/getBalance'
    URL_MONTHLY_CONSUMPTION = '/getCustomerMonthlyConsumption'
    URL_RECHARGE_HISTORY = '/getRechargeHistory'
    
    MONTHS_12 = 365
    MONTHS_11 = 335
    
    def __init__(self, accountid):
        self.accountid = accountid
        
    def _make_request(self, api_endpoint, params={}):
        account = {
            'accountNo': self.accountid,
        }
        response = requests.get(self.URL_BASE + api_endpoint, params={**account, **params}, verify=False)
        return response.json()

    def get_balance(self):
        response = self._make_request(self.URL_BALANCE)
        data = []
        for name in response['data']:
            data.append([name, str(response['data'][name])])
        return data

    def get_customer_info(self):
        response = self._make_request(self.URL_CUSTOMER_INFO)
        data = []
        for name in response['data']:
            data.append([name, str(response['data'][name])])
        return data
    
    def get_recharge_history(self):
        params = {
            'dateFrom': (datetime.now()-timedelta(days=self.MONTHS_11)).strftime("%Y-%m-%d"),
            'dateTo': datetime.now().strftime("%Y-%m-%d"),
        }
        response = self._make_request(self.URL_RECHARGE_HISTORY, params)
        data = []
        headers = ['rechargeDate', 'totalAmount', 'vat', 'energyAmount']
        for recharge in response['data']:
            data.append([
                recharge['rechargeDate'],
                recharge['totalAmount'],
                recharge['VAT'],
                recharge['energyAmount'],
                ])
        return data, headers

    def get_monthly_consumption(self):
        params = {
            'monthFrom': (datetime.now()-timedelta(days=self.MONTHS_11)).strftime("%Y-%m"),
            'monthTo': datetime.now().strftime("%Y-%m"),
        }
        response = self._make_request(self.URL_MONTHLY_CONSUMPTION, params)
        data = []
        headers = ['month', 'consumedTaka', 'consumedUnit', 'maximumDemand']
        for recharge in response['data']:
            data.append([
                recharge['month'],
                recharge['consumedTaka'],
                recharge['consumedUnit'],
                recharge['maximumDemand'],
                ])
        return data, headers
