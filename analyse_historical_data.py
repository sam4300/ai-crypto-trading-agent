from pathlib import Path
import pandas as pd
from crypto_agent.indicators import calculate_sma

def main():
    file_path = Path("data/raw/btc_usdt_1h.csv")

    df = pd.read_csv(file_path, parse_dates=["timestamp"])

    df = df.sort_values("timestamp").reset_index(drop = True)
    result = calculate_sma(df, window= 3)
    print(result[["timestamp", "close", "sma_3"]])


if __name__ == "__main__":
    main()
