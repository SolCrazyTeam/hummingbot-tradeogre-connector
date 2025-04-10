# import asyncio
# import hummingbot.connector.exchange.tradeogre.tradeogre_constants as CONSTANTS
# from unittest import TestCase
# from hummingbot.core.api_throttler.async_throttler import AsyncThrottler
# from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory
# from hummingbot.core.web_assistant.connections.data_types import RESTMethod
# from hummingbot.connector.exchange.tradeogre import (
#     tradeogre_ex_constants as CONSTANTS,
#     tradeogre_ex_constants as web_utils,
# )


# def create_throttler() -> AsyncThrottler:
#     return AsyncThrottler(CONSTANTS.RATE_LIMITS)


# def build_api_factory_without_time_synchronizer_pre_processor(throttler: AsyncThrottler) -> WebAssistantsFactory:
#     api_factory = WebAssistantsFactory(throttler=throttler)
#     return api_factory


# class TradeogreOrderBookTests(TestCase):

#     async def test_snapshot_message_from_exchange(self):
#         self.assertEqual(1, 2)

#     # Create throttler and API factory
#     async def test_api_request(self):
#         # Create a throttler and API factory
#         # Note: In a real-world scenario, you would want to use a proper event loop and not run this in a blocking way.
#         throttler = create_throttler()
#         api_factory = build_api_factory_without_time_synchronizer_pre_processor(throttler=throttler)
#         rest_assistant = await api_factory.get_rest_assistant()

#     # Make the API request
#     async def test_market_url(self):
#     markets_url = web_utils.public_rest_url(path_url="/markets")
#     markets_response = await rest_assistant.execute_request(
#         url=markets_url, method=RESTMethod.GET, throttler_limit_id="/markets"
#     )

#     print(markets_response)
#     self.assertEqual(1, 2)
