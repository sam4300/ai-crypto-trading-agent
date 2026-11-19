import pandas as pd
from crypto_agent.strategy import generate_sma_signals
from crypto_agent.backtesting import run_backtest

def main():
    df = pd.read_csv(
        "data/raw/btc_usdt_1h.csv",
        parse_dates=["timestamp"]
    )

    df = df.sort_values("timestamp").reset_index(drop=True)

    windows = [3 , 10, 20]
    warmup = max(windows)

    for window in windows:
        signals_df = generate_sma_signals(df, window= window)
        test_df = signals_df.iloc[warmup:].copy()
        result = run_backtest(test_df)

        print(f"\nSMA({window})")
        print(f"Final value: {result['final_value']:,.2f} USDT")
        print(f"Profit/Loss: {result['profit_loss']:,.2f} USDT")
        print(f"Transactions: {len(result['trades'])}")

    initial_cash = 10000.00
    fee_rate = 0.001

    entry_price = df["open"].iloc[warmup]
    final_price = df["close"].iloc[-1]

    btc_bought = (
    initial_cash * (1-fee_rate)
    )/ entry_price

    buy_hold_final = btc_bought * final_price

    buy_hold_profit = buy_hold_final - initial_cash

    print("\nBUY AND HOLD")
    print(f"Final value: {buy_hold_final:,.2f} USDT")
    print(f"Profit/Loss: {buy_hold_profit:,.2f} USDT")
    print("Transactions: 1")

if __name__ == "__main__":
    main()