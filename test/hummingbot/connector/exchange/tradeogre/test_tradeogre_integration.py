import asyncio
import unittest
from logging import Logger, LogRecord

from unittest import TestCase

from hummingbot.connector.exchange.tradeogre.tradeogre_constants import MARKETS_URL
from hummingbot.core.web_assistant.connections.data_types import RESTMethod, RESTRequest
from hummingbot.connector.exchange.tradeogre import tradeogre_web_utils as WebUtils

class TradeogreOrderBookTests(TestCase):

    async def test_snapshot_message_from_exchange(self):
        self.assertEqual(1, 2)
        
        # Create throttler and API factory
        throttler = WebUtils.create_throttler()
        api_factory = WebUtils.build_api_factory_without_time_synchronizer_pre_processor(throttler=throttler)
        rest_assistant = await api_factory.get_rest_assistant()
        
        # Make the API request
        markets_url = WebUtils.public_rest_url(path_url=MARKETS_URL)
        markets_response = await rest_assistant.execute_request(
            url=markets_url,
            method=RESTMethod.GET,
            throttler_limit_id=MARKETS_URL
        )
        
        print(markets_response)
        self.assertEqual(1, 2)

if __name__ == "__main__":
    unittest.main()
