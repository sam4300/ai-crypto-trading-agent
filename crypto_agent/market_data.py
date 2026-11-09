import ccxt
import pandas as pd
def get_crypto_price(exchange: ccxt.Exchange, symbol: str) -> float:
    """Retrieve and validate the latest traded price."""
    if symbol not in exchange.markets:
        raise ValueError(f"Unsupported trading pair: {symbol}")
    ticker = exchange.fetch_ticker(symbol)
    price = ticker.get("last")
    if price is None or price <=0:
        raise ValueError(f"Invalid price received for {symbol}")

    return float(price)

def get_historical_data(
        exchange: ccxt.Exchange,
        symbol: str, 
        timeframe : str = "1h", 
        limit: int = 10) -> pd.DataFrame:
    """Retrieve historical OHLCV data as a Pandas Dataframe"""
    candles = exchange.fetch_ohlcv(
        symbol,
        timeframe = timeframe,
        limit = limit
    )
    columns = [
        "timestamp", "open", "high", "low", "close", "volume"
    ]
    df = pd.DataFrame(candles, columns=columns)
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        unit= "ms",
        utc= True
    )

    return df
