from datetime import datetime, timedelta
import os
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.historical import CryptoHistoricalDataClient
import matplotlib.pyplot as plt

client = CryptoHistoricalDataClient(os.getenv('ALPACA_API_KEY'), os.getenv('ALPACA_SECRET_KEY'))

# Creating request object with real-time updates
request_params = CryptoBarsRequest(
  symbol_or_symbols=["BTC/USD"],
  timeframe=TimeFrame.Minute,
  start=datetime.now() - timedelta(minutes=20),  # Start from 20 minutes ago
  end=None  # End is None for real-time updates
)

plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(10, 5))

while True:
    # Fetch new data
    btc_bars = client.get_crypto_bars(request_params)
    
    # Extracting dates and prices from the data structure
    btc_data = btc_bars['BTC/USD']
    dates = [entry.timestamp for entry in btc_data]
    prices = [entry.close for entry in btc_data]
    
    # Update the plot
    ax.clear()  # Clear the previous plot
    ax.plot(dates, prices)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('BTC/USD Prices')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.draw()
    print("updated plot, last data: ", dates[-1], prices[-1])
    plt.pause(60)  # Adjust pause duration to match the timeframe
    
