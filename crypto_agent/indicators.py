import pandas as pd

def calculate_sma(
        df: pd.DataFrame,
        window: int = 3
)-> pd.DataFrame:
    """
    Return a DataFrame with a Simple Moving Average column
    """

    if window <1:
        raise ValueError("SMA must be positive")
    result = df.copy()
    result[f"sma_{window}"] = (
        result["close"].rolling(window= window).mean()
    )

    return result