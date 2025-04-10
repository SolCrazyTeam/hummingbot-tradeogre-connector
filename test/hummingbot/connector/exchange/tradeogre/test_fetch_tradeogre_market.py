import pytest

from hummingbot.connector.exchange.tradeogre.tradeogre_web_utils import TradeogreWebUtils
from hummingbot.connector.exchange.tradeogre.tradeogre_constants import MARKETS_URL


@pytest.mark.asyncio
async def test_fetch_tradeogre_markets():
    response = await TradeogreWebUtils.api_request(MARKETS_URL)
    assert isinstance(response, list)
    assert len(response) > 0
    first_market = response[0]
    print("\nFirst market data:", first_market)
    for market_dict in response:
        for market, info in market_dict.items():
            assert "price" in info
            assert "volume" in info
