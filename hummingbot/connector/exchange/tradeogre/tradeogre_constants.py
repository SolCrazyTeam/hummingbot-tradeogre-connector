from hummingbot.core.api_throttler.data_types import RateLimit
from hummingbot.core.data_type.in_flight_order import OrderState

# REST API endpoints
BASE_URL = "https://tradeogre.com/api/v1"
MARKETS_URL = "/markets"
ORDERS_URL = "/orders"
TICKER_URL = "/ticker"
ORDER_BOOK_URL = "/orders"
BALANCE_URL = "/account/balances"

# WebSocket endpoints
WS_URL = "wss://tradeogre.com/ws"  # If TradeOgre offers WebSocket support

# Rate limits
RATE_LIMITS = [
    RateLimit(limit_id=MARKETS_URL, limit=10, time_interval=1),
    RateLimit(limit_id=ORDERS_URL, limit=10, time_interval=1),
    # Add other rate limits based on TradeOgre's documentation
]

# Order states mapping
ORDER_STATE = {
    "open": OrderState.OPEN,
    "filled": OrderState.FILLED,
    "cancelled": OrderState.CANCELED,
    # Add other states based on TradeOgre's order states
}