
import pandas as pd
import pytest

from crypto_agent.indicators import calculate_sma


def test_calculate_sma():
    df = pd.DataFrame({
        "close": [100, 110, 105, 120]
    })

    result = calculate_sma(df, window=3)

    assert pd.isna(result["sma_3"].iloc[0])
    assert pd.isna(result["sma_3"].iloc[1])

    assert result["sma_3"].iloc[2] == 105.0
    assert result["sma_3"].iloc[3] == pytest.approx(111.6667, rel=1e-4)

    assert "sma_3" not in df.columns


def test_invalid_sma_window():
    df = pd.DataFrame({
        "close": [100, 110, 105]
    })

    with pytest.raises(ValueError):
        calculate_sma(df, window=0)
