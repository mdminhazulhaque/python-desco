"""
Desco Prepaid Python Client

A Python package for interacting with Dhaka Electric Supply Company Limited (DESCO)
prepaid electricity account API endpoints.

Example:
    >>> from desco import DescoPrepaid
    >>> client = DescoPrepaid("your_account_number")
    >>> balance = client.get_balance()
    >>> print(balance)
"""

from .desco import DescoPrepaid

__version__ = "0.1.0"
__author__ = "Md Minhazul Haque"
__email__ = "mdminhazulhaque@gmail.com"

__all__ = ["DescoPrepaid"]