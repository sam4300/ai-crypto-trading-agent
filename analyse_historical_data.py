from pathlib import Path
import pandas as pd
from crypto_agent.strategy import generate_sma_signals

def main():
    file_path = Path("data/raw/btc_usdt_1h.csv")

    df = pd.read_csv(file_path, parse_dates=["timestamp"])

    df = df.sort_values("timestamp").reset_index(drop = True)
    result = generate_sma_signals(df, window= 3)
    print(result[["timestamp", "close", "sma_3", "signal"]])


if __name__ == "__main__":
    main()
