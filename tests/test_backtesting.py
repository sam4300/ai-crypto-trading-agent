import pandas as pd

from crypto_agent.backtesting import run_backtest

def test_buy_and_sell_with_fees():
    df = pd.DataFrame({
        "timestamp": pd.date_range(
            "2026-01-01", periods=4, freq="h", tz="UTC"

        ),
        "open": [90,100,110,120],
        "close": [95, 105, 115, 125],
        "signal": ["BUY", "HOLD", "SELL", "HOLD"]

    })

    result = run_backtest(df, initial_cash= 1000, fee_rate= 0.001)

    assert result["initial_cash"] == 1000
    assert result["final_value"] == 1197.60
    assert result["profit_loss"] == 197.60

    assert len(result["trades"]) == 2

    assert result["trades"][0]["action"] == "BUY"
    assert result["trades"][0]["price"] == 100

    assert result["trades"][1]["action"] == "SELL"
    assert result["trades"][1]["price"] == 120

def test_open_position_final_value():
    df = pd.DataFrame({
        "timestamp": pd.date_range(
            "2026-01-01", periods=3, freq="h", tz="UTC"
        ),
        "open": [90, 100, 105],
        "close": [95, 105, 110],
        "signal": ["BUY", "HOLD", "HOLD"]
    })

    result = run_backtest(df, initial_cash=1000, fee_rate=0.001)

    assert result["final_value"] == 1098.90
    assert result["profit_loss"] == 98.90
    assert len(result["trades"]) == 1
