import pandas as pd

def generate_forecast(results, steps=30, exog_future=None):
    forecast = results.get_forecast(steps=steps, exog=exog_future)
    forecast_df = forecast.summary_frame()
    
    return forecast_df

