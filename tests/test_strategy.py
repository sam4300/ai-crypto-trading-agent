import pandas as pd
import pytest

from crypto_agent.strategy import generate_sma_signals

def test_generate_sma_signals():
    df = pd.DataFrame({
        "close": [100, 100, 100, 120, 120, 90, 90, 110]
    })

    result = generate_sma_signals(df, window=3)

    expected_signals = ["HOLD",
                        "HOLD",
                        "HOLD",
                        "BUY",
                        "HOLD",
                        "SELL",
                        "HOLD",
                        "BUY"]

    assert result["signal"].tolist() == expected_signals
    assert "signal" not in df.columns
    assert "sma_3" not in df.columns


def test_invalid_strategy_window():
    df = pd.DataFrame({
        "close": [100,110,120]
    })

    with pytest.raises(ValueError):
        generate_sma_signals(df, window = 0)