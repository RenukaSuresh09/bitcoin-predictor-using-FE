from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_sarimax_model(df, order=(1,1,1), seasonal_order=(1,1,1,7), exog_features=None):
    y = df['Close']
    exog = df[exog_features] if exog_features else None
    
    model = SARIMAX(y, order=order, seasonal_order=seasonal_order, exog=exog, enforce_stationarity=False, enforce_invertibility=False)
    results = model.fit(disp=False)
    
    print(results.summary())
    
    return model, results
