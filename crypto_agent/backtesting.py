
import pandas as pd


def run_backtest(
    df: pd.DataFrame,
    initial_cash: float = 10000.0,
    fee_rate: float = 0.001
) -> dict:

    cash = initial_cash
    btc = 0.0
    trades = []

    for i in range(1, len(df)):

        signal = df["signal"].iloc[i - 1]
        price = df["open"].iloc[i]

        if signal == "BUY" and btc == 0 and cash > 0:

            btc = (cash * (1 - fee_rate)) / price
            cash = 0.0

            trades.append({
                "action": "BUY",
                "price": price,
                "timestamp": df["timestamp"].iloc[i]
            })

        elif signal == "SELL" and btc > 0:

            cash = btc * price * (1 - fee_rate)
            btc = 0.0

            trades.append({
                "action": "SELL",
                "price": price,
                "timestamp": df["timestamp"].iloc[i]
            })

    final_value = cash + btc * df["close"].iloc[-1]

    return {
        "initial_cash": initial_cash,
        "final_value": round(final_value, 2),
        "profit_loss": round(final_value - initial_cash, 2),
        "trades": trades
    }
