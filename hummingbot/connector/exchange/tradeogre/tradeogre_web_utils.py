from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union, Callable
import hummingbot.connector.exchange.tradeogre.tradeogre_constants as CONSTANTS
from hummingbot.connector.time_synchronizer import TimeSynchronizer
from hummingbot.connector.utils import TimeSynchronizerRESTPreProcessor
from hummingbot.core.api_throttler.async_throttler import AsyncThrottler
from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import RESTMethod
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory
from hummingbot.connector.exchange_py_base import ExchangePyBase

import hummingbot.connector.exchange.tradeogre.tradeogre_constants as CONSTANTS

if TYPE_CHECKING:
    from hummingbot.client.config.config_helpers import ClientConfigAdapter

class TradeogreWebUtils:
    @staticmethod
    async def api_request(method: str, path_url: str, domain: str = CONSTANTS.DEFAULT_DOMAIN, **kwargs):
        """
        Sends an HTTP request to the TradeOgre API
        :param method: HTTP method (GET, POST, etc.)
        :param path_url: API endpoint path
        :param domain: the domain to connect to
        :return: JSON response from the API
        """
        throttler = create_throttler()
        api_factory = build_api_factory_without_time_synchronizer_pre_processor(throttler=throttler)
        rest_assistant = await api_factory.get_rest_assistant()
        
        url = public_rest_url(path_url=path_url, domain=domain)
        
        response = await rest_assistant.execute_request(
            url=url,
            method="GET",
            throttler_limit_id=path_url,
            **kwargs
        )
        
        return response


async def api_markets_infos() -> Union[str, Dict[str, Any]]:
    throttler = create_throttler()
    api_factory = build_api_factory_without_time_synchronizer_pre_processor(throttler=throttler)
    rest_assistant = await api_factory.get_rest_assistant()
    rest_assistant._throttler
    url = public_rest_url(path_url="/markets", domain=CONSTANTS.DEFAULT_DOMAIN)
    response = await rest_assistant.execute_request(
        url=url,
        method=RESTMethod.GET,
        throttler_limit_id=CONSTANTS.SERVER_MARKETS_PATH_URL
    )    
    return response

def public_rest_url(path_url: str, domain: str = CONSTANTS.DEFAULT_DOMAIN) -> str:
    """
    Creates a full URL for provided public REST endpoint
    :param path_url: a public REST endpoint
    :param domain: the Tradeogre domain to connect to ("com" or "us"). The default value is "com"
    :return: the full URL to the endpoint
    """
    return CONSTANTS.REST_URL.format(domain) + CONSTANTS.PUBLIC_API_VERSION + path_url


def private_rest_url(path_url: str, domain: str = CONSTANTS.DEFAULT_DOMAIN) -> str:
    """
    Creates a full URL for provided private REST endpoint
    :param path_url: a private REST endpoint
    :param domain: the Tradeogre domain to connect to ("com" or "us"). The default value is "com"
    :return: the full URL to the endpoint
    """
    return CONSTANTS.REST_URL.format(domain) + CONSTANTS.PRIVATE_API_VERSION + path_url


def build_api_factory(
        throttler: Optional[AsyncThrottler] = None,
        time_synchronizer: Optional[TimeSynchronizer] = None,
        domain: str = CONSTANTS.DEFAULT_DOMAIN,
        time_provider: Optional[Callable] = None,
        auth: Optional[AuthBase] = None, ) -> WebAssistantsFactory:
    throttler = throttler or create_throttler()
    time_synchronizer = time_synchronizer or TimeSynchronizer()
    time_provider = time_provider or (lambda: get_current_server_time(
        throttler=throttler,
        domain=domain,
    ))
    api_factory = WebAssistantsFactory(
        throttler=throttler,
        auth=auth,
        rest_pre_processors=[
            TimeSynchronizerRESTPreProcessor(synchronizer=time_synchronizer, time_provider=time_provider),
        ])
    return api_factory


def build_api_factory_without_time_synchronizer_pre_processor(throttler: AsyncThrottler) -> WebAssistantsFactory:
    api_factory = WebAssistantsFactory(throttler=throttler)
    return api_factory

async def get_current_server_time(
        throttler: Optional[AsyncThrottler] = None,
        domain: str = CONSTANTS.DEFAULT_DOMAIN,
) -> float:
    throttler = throttler or create_throttler()
    api_factory = build_api_factory_without_time_synchronizer_pre_processor(throttler=throttler)
    rest_assistant = await api_factory.get_rest_assistant()
    response = await rest_assistant.execute_request(
        url=public_rest_url(path_url=CONSTANTS.SERVER_TIME_PATH_URL, domain=domain),
        method=RESTMethod.GET,
        throttler_limit_id=CONSTANTS.SERVER_TIME_PATH_URL,
    )
    server_time = response["serverTime"]
    return server_time

def create_throttler() -> AsyncThrottler:
    throttler = AsyncThrottler(CONSTANTS.RATE_LIMITS)
    return throttler
