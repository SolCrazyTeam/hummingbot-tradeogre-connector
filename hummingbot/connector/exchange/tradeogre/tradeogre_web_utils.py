import aiohttp
import ujson
from typing import Dict, Any

from hummingbot.connector.exchange.tradeogre.tradeogre_constants import BASE_URL

class TradeOgreWebUtils:
    @staticmethod
    async def api_request(
        http_method: str,
        path_url: str,
        params: Dict[str, Any] = None,
        data: Dict[str, Any] = None,
        headers: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        """
        Sends an API request to TradeOgre
        """
        url = f"{BASE_URL}{path_url}"
        
        client = aiohttp.ClientSession()
        
        try:
            if http_method == "GET":
                response = await client.get(url, params=params, headers=headers)
            elif http_method == "POST":
                response = await client.post(url, json=data, headers=headers)
            # Add other HTTP methods as needed
            
            response_json = await response.json()
            return response_json
        except Exception as e:
            # Handle exceptions
            raise e
        finally:
            await client.close()