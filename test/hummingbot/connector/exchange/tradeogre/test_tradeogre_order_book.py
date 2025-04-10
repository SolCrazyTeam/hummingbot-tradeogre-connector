import asyncio
import unittest
from logging import Logger, LogRecord

from unittest import TestCase
from hummingbot.connector.exchange.tradeogre.tradeogre_constants import MARKETS_URL

from hummingbot.connector.exchange.tradeogre import tradeogre_web_utils as WebUtils

from hummingbot.core.data_type.order_book_message import OrderBookMessageType
from hummingbot.connector.exchange.binance.binance_exchange import BinanceExchange

class TradeogreOrderBookTests(TestCase):

    async def test_snapshot_message_from_exchange(self):
        markets_response = await WebUtils.api_request("GET", MARKETS_URL)
        print(markets_response)
        self.assertEqual(1, 2)

        # # Parse the response to extract prices for each trading pair
        # for market_data in markets_response:
        #     for market_name, market_info in market_data.items():
        #         a = 1

        # snapshot_message = MexcOrderBook.snapshot_message_from_exchange(
        #     msg={
        #         "lastUpdateId": 1,
        #         "bids": [
        #             ["4.00000000", "431.00000000"]
        #         ],
        #         "asks": [
        #             ["4.00000200", "12.00000000"]
        #         ]
        #     },
        #     timestamp=1640000000.0,
        #     metadata={"trading_pair": "COINALPHA-HBOT"}
        # )

        # self.assertEqual("COINALPHA-HBOT", snapshot_message.trading_pair)
        # self.assertEqual(OrderBookMessageType.SNAPSHOT, snapshot_message.type)
        # self.assertEqual(1640000000.0, snapshot_message.timestamp)
        # self.assertEqual(1, snapshot_message.update_id)
        # self.assertEqual(-1, snapshot_message.trade_id)
        # self.assertEqual(1, len(snapshot_message.bids))
        # self.assertEqual(4.0, snapshot_message.bids[0].price)
        # self.assertEqual(431.0, snapshot_message.bids[0].amount)
        # self.assertEqual(1, snapshot_message.bids[0].update_id)
        # self.assertEqual(1, len(snapshot_message.asks))
        # self.assertEqual(4.000002, snapshot_message.asks[0].price)
        # self.assertEqual(12.0, snapshot_message.asks[0].amount)
        # self.assertEqual(1, snapshot_message.asks[0].update_id)

if __name__ == "__main__":
    unittest.main()
