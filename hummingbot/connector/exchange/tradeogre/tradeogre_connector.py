from hummingbot.connector.connector_base import ConnectorBase
from hummingbot.core.data_type.order_book_tracker import OrderBookTracker
from hummingbot.client.config.config_data_types import ClientConfigAdapter
from hummingbot.core.utils.trading_pair_fetcher import TradingPairFetcher

class TradeOgreConnector(ConnectorBase):
    # def __init__(self):
    #     super().__init__()
    #     self._trading_pairs = []
    #     self._order_book_tracker = OrderBookTracker()
    #     self._ready = False

    # @property
    # def name(self) -> str:
    #     return "TradeOgre"

    # @property
    # def ready(self) -> bool:
    #     return self._ready

    # def start(self):
    #     self._ready = True
    #     self.logger().info("TradeOgreConnector started.")

    # def stop(self):
    #     self._ready = False
    #     self.logger().info("TradeOgreConnector stopped.")

    # def tick(self):
    #     pass  # you can implement periodic logic here
    def __init__(self, client_config_map: ClientConfigAdapter):
        super().__init__()
        self._api_key = client_config_map.get("tradeogre_exchange_api_key")
        self._secret_key = client_config_map.get("tradeogre_exchange_secret_key")
        self._ready = False
