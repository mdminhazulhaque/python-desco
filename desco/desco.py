#!/usr/bin/env python3
"""
DESCO (Dhaka Electric Supply Company) prepaid API client.

Stateless core engine: construct with an account number, call methods, get back
plain dicts (or lists of dicts). No authentication is required by this API and
no file/env I/O happens here, so the class is safe to instantiate per-request
inside FastAPI, Django, or any web framework. See the `examples/` directory.
"""

from datetime import timedelta, datetime
from typing import List, Dict, Any

import requests
import urllib3

# The DESCO endpoint presents a certificate that fails default verification.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DescoPrepaid:
    """Client for the DESCO prepaid electricity account API (no auth required)."""

    BASE_URL = "https://prepaid.desco.org.bd/api/tkdes/customer"
    ENDPOINTS = {
        "customer_info": "/getCustomerInfo",
        "balance": "/getBalance",
        "monthly_consumption": "/getCustomerMonthlyConsumption",
        "recharge_history": "/getRechargeHistory",
    }
    DEFAULT_HISTORY_DAYS = 335  # ~11 months
    TIMEOUT = 30

    def __init__(self, account_id: str) -> None:
        self.account_id = str(account_id)

    def _make_request(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        request_params = {"accountNo": self.account_id, **(params or {})}
        response = requests.get(
            f"{self.BASE_URL}{endpoint}",
            params=request_params,
            verify=False,
            timeout=self.TIMEOUT,
        )
        response.raise_for_status()
        return response.json()

    def get_balance(self) -> Dict[str, Any]:
        """Return current balance / consumption as a dict."""
        return self._make_request(self.ENDPOINTS["balance"]).get("data", {})

    def get_customer_info(self) -> Dict[str, Any]:
        """Return customer/meter details as a dict."""
        return self._make_request(self.ENDPOINTS["customer_info"]).get("data", {})

    def get_recharge_history(self) -> List[Dict[str, Any]]:
        """Return recharge history as a list of dicts."""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=self.DEFAULT_HISTORY_DAYS)
        params = {
            "dateFrom": start_date.strftime("%Y-%m-%d"),
            "dateTo": end_date.strftime("%Y-%m-%d"),
        }
        response = self._make_request(self.ENDPOINTS["recharge_history"], params)
        return [
            {
                "recharge_date": r.get("rechargeDate"),
                "total_amount": r.get("totalAmount"),
                "vat": r.get("VAT"),
                "energy_amount": r.get("energyAmount"),
            }
            for r in response.get("data", [])
        ]

    def get_monthly_consumption(self) -> List[Dict[str, Any]]:
        """Return monthly consumption history as a list of dicts."""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=self.DEFAULT_HISTORY_DAYS)
        params = {
            "monthFrom": start_date.strftime("%Y-%m"),
            "monthTo": end_date.strftime("%Y-%m"),
        }
        response = self._make_request(self.ENDPOINTS["monthly_consumption"], params)
        return [
            {
                "month": c.get("month"),
                "consumed_taka": c.get("consumedTaka"),
                "consumed_unit": c.get("consumedUnit"),
                "maximum_demand": c.get("maximumDemand"),
            }
            for c in response.get("data", [])
        ]
