from unittest.mock import Mock
from crypto_agent.market_data import get_crypto_price

def test_valid_crypto_price():
    exchange = Mock()
    exchange.markets = {"BTC/USDT":{}}

    exchange.fetch_ticker.return_value = {"last": 76776.90}
    price = get_crypto_price(exchange, "BTC/USDT")

    assert price == 76776.90
    exchange.fetch_ticker.assert_called_once_with("BTC/USDT")