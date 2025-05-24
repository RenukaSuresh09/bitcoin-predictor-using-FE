import pandas as pd

def load_and_prepare_data(bitcoin_path, exog_path=None):
    # Load Bitcoin price data
    df = pd.read_csv(bitcoin_path, parse_dates=['Date'], index_col='Date')
    df.sort_index(inplace=True)
    
    # Feature Engineering: Lag features
    df['lag_1'] = df['Close'].shift(1)
    df['rolling_mean_7'] = df['Close'].rolling(window=7).mean()
    df['rolling_std_7'] = df['Close'].rolling(window=7).std()
    
    # Exogenous variables (optional)
    if exog_path:
        exog = pd.read_csv(exog_path, parse_dates=['Date'], index_col='Date')
        df = df.join(exog, how='left')
    
    # Drop rows with NaN values from lags
    df.dropna(inplace=True)
    
    return df

