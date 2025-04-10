from decimal import Decimal
from typing import Any, Dict

from pydantic import Field, SecretStr

from hummingbot.client.config.config_data_types import BaseConnectorConfigMap, ClientFieldData
from hummingbot.core.data_type.trade_fee import TradeFeeSchema

CENTRALIZED = True
EXAMPLE_PAIR = "ZRX-ETH"

DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.001"),
    taker_percent_fee_decimal=Decimal("0.001"),
    buy_percent_fee_deducted_from_returns=True
)


def is_exchange_information_valid(exchange_info: Dict[str, Any]) -> bool:
    """
    Verifies if a trading pair is enabled to operate with based on its exchange information
    :param exchange_info: the exchange information for a trading pair
    :return: True if the trading pair is enabled, False otherwise
    """
    is_spot = False
    is_trading = False

    if exchange_info.get("status", None) == "TRADING":
        is_trading = True

    permissions_sets = exchange_info.get("permissionSets", list())
    for permission_set in permissions_sets:
        # PermissionSet is a list, find if in this list we have "SPOT" value or not
        if "SPOT" in permission_set:
            is_spot = True
            break

    return is_trading and is_spot


class TradeogreConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="tradeogre", const=True, client_data=None)
    tradeogre_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Tradeogre API key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )
    tradeogre_api_secret: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Tradeogre API secret",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )

    class Config:
        title = "tradeogre"


KEYS = TradeogreConfigMap.construct()

OTHER_DOMAINS = ["tradeogre_us"]
OTHER_DOMAINS_PARAMETER = {"tradeogre_us": "us"}
OTHER_DOMAINS_EXAMPLE_PAIR = {"tradeogre_us": "BTC-USDT"}
OTHER_DOMAINS_DEFAULT_FEES = {"tradeogre_us": DEFAULT_FEES}


class TradeogreUSConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="tradeogre_us", const=True, client_data=None)
    tradeogre_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Tradeogre US API key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )
    tradeogre_api_secret: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Tradeogre US API secret",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )

    class Config:
        title = "tradeogre_us"


OTHER_DOMAINS_KEYS = {"tradeogre_us": TradeogreUSConfigMap.construct()}
