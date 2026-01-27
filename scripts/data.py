import pandas as pd
import numpy as np

# Define parameters
start_date = '2025-01-01'
periods = 365
frequency = 'D'

# Create time index
time_index = pd.date_range(start=start_date, periods=periods, freq=frequency)

# Generate synthetic data: trend + seasonality + noise
trend = np.linspace(0, 10, periods)  # Linear trend
seasonality = 10 * np.sin(2 * np.pi * np.arange(periods) / 365)  # Annual cycle
noise = np.random.normal(0, 2, periods)  # Gaussian noise

# Combine components
mobile = trend + seasonality + noise

noise = np.random.normal(0, 2, periods)  # Gaussian noise
desktop = trend + seasonality + noise

# Create DataFrame
df = pd.DataFrame({'mobile': mobile, 'desktop':desktop}, index=time_index)
df.index.name = 'date'
df.to_csv("visitor_data.csv")
print(df)
