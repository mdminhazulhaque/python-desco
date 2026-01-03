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

# Version will be updated by GitHub Actions during release
__version__ = "1.0.0"
__author__ = "Md Minhazul Haque"
__email__ = "mdminhazulhaque@gmail.com"

__all__ = ["DescoPrepaid"]