import hashlib
import hmac
import time
import base64
import logging

from typing import Any, Dict

from hummingbot.connector.exchange.tradeogre import tradeogre_constants as CONSTANTS
from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import RESTRequest, WSRequest

def convert_to_base64(input_str: str) -> str:
    # Encode the string to bytes, then convert to base64
    byte_data = input_str.encode('utf-8')
    base64_bytes = base64.b64encode(byte_data)
    return base64_bytes.decode('utf-8')

class TradeogreAuth(AuthBase):
    """
    Auth class required by Tradeogre API
    Learn more at https://Tradeogre.github.io/Tradeogre-pro-api/#authenticate-a-restful-request
    """

    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    async def rest_authenticate(self, request: RESTRequest) -> RESTRequest:
        """
        Adds the server time and the signature to the request, required for authenticated interactions. It also adds
        the required parameter in the request header.
        :param request: the request to be configured for authenticated interaction
        """
        # Generates auth headers
        path = request.throttler_limit_id
        headers_auth = self.get_auth_headers(path)

        headers = {}
        if request.headers is not None:
            headers.update(request.headers)
        headers.update(headers_auth)
        request.headers = headers

        return request

    async def ws_authenticate(self, request: WSRequest) -> WSRequest:
        """
        This method is intended to configure a websocket request to be authenticated. Tradeogre does not use this
        functionality
        """
        return request  # pass-through

    def get_auth_headers(self, path_url: str, data: Dict[str, Any] = None):
        """
        Generates authentication signature and return it in a dictionary along with other inputs
        :param path_url: URL of the auth API endpoint
        :param data: data to be included in the headers
        :return: a dictionary of request info including the request signature
        """
        logging.getLogger().error(f"key={self.api_key},{self.secret_key}")
        signature = convert_to_base64(f"{self.api_key}:{self.secret_key}")
        token = f"Basic {signature}"
        logging.getLogger().error(f"token={token}")
        return {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": token,
        }

    def _time(self) -> float:
        return time.time()
