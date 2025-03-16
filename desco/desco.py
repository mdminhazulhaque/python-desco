#!/usr/bin/env python3

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