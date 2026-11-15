import pandas as pd
from crypto_agent.indicators import calculate_sma

def generate_sma_signals(
        df: pd.DataFrame,
        window: int = 3
)-> pd.DataFrame:
    """Generate trading signals using SMA crossovers."""

    result = calculate_sma(df, window= window)
    sma = result[f"sma_{window}"]
    close = result["close"]

    previous_sma = sma.shift(1)
    previous_close = close.shift(1)

    buy_condition = (
        (previous_close <= previous_sma) & (close> sma)
    )

    sell_condition = ((previous_close >= previous_sma) &
                      (close < sma)
                      )

    result["signal"] = "HOLD"

    result.loc[buy_condition, "signal"] = "BUY"
    result.loc[sell_condition, "signal"] = "SELL"

    return result
