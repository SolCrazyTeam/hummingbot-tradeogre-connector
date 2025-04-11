# import asyncio
from unittest import TestCase

import requests
from requests.auth import HTTPBasicAuth

# from typing_extensions import Awaitable

buyurl = "https://tradeogre.com/api/v1/order/buy"
sellurl = "https://tradeogre.com/api/v1/order/sell"


class TradeogreAuthTests(TestCase):

    print("----------Buy/Sell Order Test Start--------------")

    def setUp(self) -> None:
        self._api_key = "87707534a44e375f4570c8328544adcd"
        self._secret = "9a9f2597ac03c38c7abc174c0a1bdb42"

    # def async_run_with_timeout(self, coroutine: Awaitable, timeout: float = 1):
    #     ret = asyncio.get_event_loop().run_until_complete(asyncio.wait_for(coroutine, timeout))
    #     return ret

    def test_rest_buy_order(self):
        print("----------Buy Order Test Start--------------")
        params = {
            "market": "ETH-USDT",
            "quantity": "0.1",
            "price": "1560",
            "duration": "GTC",
        }

        response = requests.post(buyurl, data=params, auth=HTTPBasicAuth(self._api_key, self._secret))
        if response.status_code == 200:
            print("Order placed successfully!")
        else:
            print("Failed to place order:", response.status_code, response.text)

        print("Response:", response.text)

    def test_rest_sell_order(self):
        print("----------SELL Order Test Start--------------")
        params = {
            "market": "ETH-USDT",
            "quantity": "0.1",
            "price": "1570",
            "duration": "GTC",
        }

        response = requests.post(sellurl, data=params, auth=HTTPBasicAuth(self._api_key, self._secret))
        if response.status_code == 200:
            print("Order placed successfully!")
        else:
            print("Failed to place order:", response.status_code, response.text)

        print("Response:", response.text)

        print("----------Test End!--------------")
