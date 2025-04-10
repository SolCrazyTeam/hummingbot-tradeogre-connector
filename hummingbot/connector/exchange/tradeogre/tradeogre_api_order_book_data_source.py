import asyncio
import logging
from typing import Dict, List, Optional, Any

from hummingbot.core.data_type import order_book
from hummingbot.core.data_type.order_book_message import OrderBookMessage
from hummingbot.core.data_type.order_book_tracker_data_source import OrderBookTrackerDataSource
from hummingbot.connector.exchange.tradeogre.tradeogre_constants import MARKETS_URL, ORDER_BOOK_URL
from hummingbot.connector.exchange.tradeogre.tradeogre_web_utils import TradeogreWebUtils

class TradeogreAPIOrderBookDataSource(OrderBookTrackerDataSource):
    def __init__(self, trading_pairs: List[str] = None):
        super().__init__(trading_pairs)
        self._logger = logging.getLogger(__name__)
        
    async def get_last_traded_prices(self, trading_pairs: List[str]) -> Dict[str, float]:
        """
        Return a dictionary the trading pair as key and the current price as value
        """
        result = {}
        markets_response = await TradeogreWebUtils.api_request("GET", MARKETS_URL)
        
        # Parse the response to extract prices for each trading pair
        for market_data in markets_response:
            for market_name, market_info in market_data.items():
                if market_name in trading_pairs:
                    result[market_name] = float(market_info["price"])
        
        return result
        
    async def get_new_order_book(self, trading_pair: str) -> order_book:
        """
        Creates a new order book for a trading pair
        """
        # Implementation depends on TradeOgre's order book data structure
        # This is a placeholder example
        order_book_response = await TradeogreWebUtils.api_request(
            "GET", 
            f"{ORDER_BOOK_URL}/{trading_pair}"
        )
        
        # Parse order book data and create an OrderBook object
        # This part is highly dependent on TradeOgre's response format
        return order_book()
        
    async def get_trading_pairs(self) -> List[str]:
        """
        Get all trading pairs from the exchange
        """
        markets_response = await TradeogreWebUtils.api_request("GET", MARKETS_URL)
        trading_pairs = []
        
        for market_data in markets_response:
            for market_name in market_data.keys():
                trading_pairs.append(market_name)
                
        return trading_pairs