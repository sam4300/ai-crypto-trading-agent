from pathlib import Path
import pandas as pd
from crypto_agent.strategy import generate_sma_signals
from crypto_agent.backtesting import run_backtest

def main():
    file_path = Path("data/raw/btc_usdt_1h.csv")

    df = pd.read_csv(file_path, parse_dates=["timestamp"])

    df = df.sort_values("timestamp").reset_index(drop = True)
    result = generate_sma_signals(df, window= 3)
    backtest = run_backtest(result)
    print(f"Starting balance: ${backtest['initial_cash']:,.2f}")
    print(f"Final portfolio value: ${backtest['final_value']:,.2f}")
    print(f"Profit/Loss: ${backtest['profit_loss']:,.2f}")
    print(f"Number of transactions: {len(backtest['trades'])}")

    for trade in backtest["trades"]:
        print(trade)
    print(result[["timestamp", "close", "sma_3", "signal"]])


if __name__ == "__main__":
    main()
