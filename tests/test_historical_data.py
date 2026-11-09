
import pandas as pd

import export_historical_data


def test_csv_export(tmp_path, monkeypatch):
    # Create fake historical data
    fake_data = pd.DataFrame({
        "timestamp": ["2026-11-09 01:00:00+00:00"],
        "open": [100.0],
        "high": [110.0],
        "low": [95.0],
        "close": [105.0],
        "volume": [2.5]
    })

    # Replace the real Kraken exchange with a fake object
    fake_exchange = object()

    monkeypatch.setattr(
        export_historical_data.ccxt,
        "kraken",
        lambda: fake_exchange
    )

    # Replace the real historical-data function
    def fake_get_historical_data(exchange, symbol, timeframe, limit):
        assert exchange is fake_exchange
        assert symbol == "BTC/USDT"
        assert timeframe == "1h"
        assert limit == 10
        return fake_data

    monkeypatch.setattr(
        export_historical_data,
        "get_historical_data",
        fake_get_historical_data
    )

    # Use a temporary directory
    monkeypatch.chdir(tmp_path)

    # Run the export function
    export_historical_data.main()

    # Verify that the CSV was created
    csv_file = tmp_path / "data/raw/btc_usdt_1h.csv"

    assert csv_file.exists()

    # Read the CSV and verify its contents
    result = pd.read_csv(csv_file)

    assert len(result) == 1
    assert result["close"].iloc[0] == 105.0
