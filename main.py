import ccxt
from crypto_agent.market_data import get_crypto_price
SYMBOLS = ("BTC/USDT", "XRP/USDT")

def main():
    exchange = ccxt.kraken({
        "enableRateLimit": True,
    })

    print("AI Crypto Trading Agent")

    try:
        exchange.load_markets()
        for symbol in SYMBOLS:
            try:
                price = get_crypto_price(exchange,symbol)
                print(f"{symbol}:  {price:,.2f} USDT")
            except ValueError as error:
                print(f"Data error: {error}")

    except ccxt.BaseError as error:
        print(f"Kraken API error: {error}")


if __name__ == "__main__":
    main()