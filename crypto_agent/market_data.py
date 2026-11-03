import ccxt
def get_crypto_price(exchange: ccxt.Exchange, symbol: str) -> float:
    """Retrieve and validate the latest traded price."""
    if symbol not in exchange.markets:
        raise ValueError(f"Unsupported trading pair: {symbol}")
    ticker = exchange.fetch_ticker(symbol)
    price = ticker.get("last")
    if price is None or price <=0:
        raise ValueError(f"Invalid price received for {symbol}")

    return float(price)