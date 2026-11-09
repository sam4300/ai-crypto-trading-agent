from unittest.mock import Mock
from crypto_agent.market_data import get_crypto_price, get_historical_data
import pandas as pd

def test_valid_crypto_price():
    exchange = Mock()
    exchange.markets = {"BTC/USDT":{}}

    exchange.fetch_ticker.return_value = {"last": 76776.90}
    price = get_crypto_price(exchange, "BTC/USDT")

    assert price == 76776.90
    exchange.fetch_ticker.assert_called_once_with("BTC/USDT")

def test_historical_data():
    exchange = Mock()
    exchange.fetch_ohlcv.return_value = [
        [1794186000000, 75293.1, 75484.3, 74713.4, 75188.3, 3.29266912],
        [1794189600000, 75160.6, 75581.7, 75150.7, 75275.4, 2.40315921]
    ]

    df = get_historical_data(exchange, "BTC/USDT", timeframe= "1h", limit= 2)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert df["close"].iloc[0] == 75188.3
    assert str(df["timestamp"].dt.tz) == "UTC"

    exchange.fetch_ohlcv.assert_called_once_with(
        "BTC/USDT",
        timeframe = "1h",
        limit = 2
    )

