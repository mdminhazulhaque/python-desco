#!/usr/bin/env python3
"""
Desco Prepaid API Client

A Python client for interacting with Dhaka Electric Supply Company Limited (DESCO)
prepaid electricity account API endpoints.
"""

import requests
from datetime import timedelta, datetime
from typing import List, Tuple, Dict, Any
import urllib3

# Disable SSL warnings for the DESCO API
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DescoPrepaid:
    """
    A client for interacting with DESCO prepaid electricity account API.
    
    This class provides methods to retrieve account balance, customer information,
    monthly consumption data, and recharge history for DESCO prepaid accounts.
    """
    
    # API Configuration
    BASE_URL = 'https://prepaid.desco.org.bd/api/tkdes/customer'
    ENDPOINTS = {
        'customer_info': '/getCustomerInfo',
        'balance': '/getBalance',
        'monthly_consumption': '/getCustomerMonthlyConsumption',
        'recharge_history': '/getRechargeHistory'
    }
    
    # Date range constants (in days)
    DEFAULT_HISTORY_DAYS = 335  # ~11 months
    
    def __init__(self, account_id: str) -> None:
        """
        Initialize the DESCO prepaid client.
        
        Args:
            account_id (str): The DESCO prepaid account number
        """
        self.account_id = str(account_id)
        
    def _make_request(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make an authenticated request to the DESCO API.
        
        Args:
            endpoint (str): The API endpoint to call
            params (dict, optional): Additional parameters for the request
            
        Returns:
            dict: The JSON response from the API
            
        Raises:
            requests.RequestException: If the API request fails
        """
        if params is None:
            params = {}
            
        # Base parameters with account number
        request_params = {
            'accountNo': self.account_id,
            **params
        }
        
        try:
            response = requests.get(
                f"{self.BASE_URL}{endpoint}",
                params=request_params,
                verify=False,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise requests.RequestException(f"Failed to fetch data from DESCO API: {e}")

    def get_balance(self) -> List[List[str]]:
        """
        Get current account balance and consumption information.
        
        Returns:
            List[List[str]]: A list of [key, value] pairs containing balance information
        """
        response = self._make_request(self.ENDPOINTS['balance'])
        
        data = []
        if 'data' in response:
            for key, value in response['data'].items():
                data.append([key, str(value)])
        
        return data

    def get_customer_info(self) -> List[List[str]]:
        """
        Get detailed customer and meter information.
        
        Returns:
            List[List[str]]: A list of [key, value] pairs containing customer information
        """
        response = self._make_request(self.ENDPOINTS['customer_info'])
        
        data = []
        if 'data' in response:
            for key, value in response['data'].items():
                data.append([key, str(value)])
        
        return data
    
    def get_recharge_history(self) -> Tuple[List[List[str]], List[str]]:
        """
        Get recharge and payment history for the account.
        
        Returns:
            tuple: A tuple containing:
                - List of recharge records as [date, amount, vat, energy_amount]
                - List of column headers
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=self.DEFAULT_HISTORY_DAYS)
        
        params = {
            'dateFrom': start_date.strftime("%Y-%m-%d"),
            'dateTo': end_date.strftime("%Y-%m-%d"),
        }
        
        response = self._make_request(self.ENDPOINTS['recharge_history'], params)
        
        headers = ['rechargeDate', 'totalAmount', 'vat', 'energyAmount']
        data = []
        
        if 'data' in response:
            for recharge in response['data']:
                data.append([
                    recharge.get('rechargeDate', ''),
                    recharge.get('totalAmount', ''),
                    recharge.get('VAT', ''),
                    recharge.get('energyAmount', ''),
                ])
        
        return data, headers

    def get_monthly_consumption(self) -> Tuple[List[List[str]], List[str]]:
        """
        Get monthly consumption history for the account.
        
        Returns:
            tuple: A tuple containing:
                - List of consumption records as [month, consumed_taka, consumed_unit, max_demand]
                - List of column headers
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=self.DEFAULT_HISTORY_DAYS)
        
        params = {
            'monthFrom': start_date.strftime("%Y-%m"),
            'monthTo': end_date.strftime("%Y-%m"),
        }
        
        response = self._make_request(self.ENDPOINTS['monthly_consumption'], params)
        
        headers = ['month', 'consumedTaka', 'consumedUnit', 'maximumDemand']
        data = []
        
        if 'data' in response:
            for consumption in response['data']:
                data.append([
                    consumption.get('month', ''),
                    consumption.get('consumedTaka', ''),
                    consumption.get('consumedUnit', ''),
                    consumption.get('maximumDemand', ''),
                ])
        
        return data, headers