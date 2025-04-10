import asyncio
import pytest
import unittest
from logging import Logger, LogRecord

import logging
logger = logging.getLogger(__name__)

from unittest import TestCase
from hummingbot.connector.exchange.tradeogre.tradeogre_constants import MARKETS_URL

from hummingbot.connector.exchange.tradeogre import tradeogre_web_utils as WebUtils
from hummingbot.connector.exchange.tradeogre.tradeogre_web_utils import TradeogreWebUtils
from hummingbot.core.data_type.order_book_message import OrderBookMessageType
from hummingbot.connector.exchange.binance.binance_exchange import BinanceExchange

pytest_plugins = ('pytest_asyncio',)

@pytest.mark.asyncio
class TestGroup:
    async def test_async(self):
        logger.debug("------------- start ------------")

        markets_response = await WebUtils.api_markets_infos()
        logger.debug(markets_response)

        await asyncio.sleep(2)

        logger.debug("------------- end ------------")

if __name__ == "__main__":
    unittest.main()
