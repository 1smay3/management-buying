"""
Handles data requests that aren't handled in the FMP-python module
"""
import requests
from app.config.Secrets import fmp_key
from app.config.Config import base_url, api_version
from typing import Optional


def foo(a: str, b: Optional[str]) -> str or None:
    pass


"""
Source: fmp-python module
"""


class FMPRequestBuilder(object):

    def __init__(self, api_key):
        self.base_url = base_url
        self.api_version = api_version
        self.api_key = api_key

    # TODO: surely this isn't the optimal way to do with the if statement... can look into the FMP module but
    #  time/return not right yet
    def get_data(self, endpoint: str, ticker: str, limit=None):
        if limit is None:
            request_url = self.base_url + self.api_version + endpoint + "?" + "symbol=" + ticker + "&apikey=" + self.api_key
        else:
            request_url = self.base_url + self.api_version + endpoint + "?" + "symbol=" + ticker + "&limit=" + limit + \
                          "&apikey=" + self.api_key
        return request_url


test = FMPRequestBuilder(fmp_key)

print(test.get_data('insider-trading', 'AAPL', "10"))
