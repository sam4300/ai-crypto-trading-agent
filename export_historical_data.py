from pathlib import Path
import ccxt
from crypto_agent.market_data import get_historical_data
def main():
    exchange = ccxt.kraken()

    df = get_historical_data(
        exchange,
        "BTC/USDT",
        timeframe= "1h",
        limit= 10
    )
    output_directory = Path("data/raw")
    output_directory.mkdir(parents= True, exist_ok= True)

    output_file = output_directory/ "btc_usdt_1h.csv"

    df.to_csv(output_file, index=False)

    print(f"Saved {len(df)} candles to {output_file}")


if __name__ == "__main__":
    main()
