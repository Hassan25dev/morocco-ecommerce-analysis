import pandas as pd

def revenue_by_region(df):
    return (
        df.groupby('region')['total_amount']
        .mean()
        .sort_values(ascending=False)
    )

def top_product_by_revenue(df):
    return (
        df.groupby('product_id')['total_amount']
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )

def monthly_average_revenue(df):
    df = df.copy()
    df.set_index('order_date', inplace=True)
    return df['total_amount'].resample('M').mean()
