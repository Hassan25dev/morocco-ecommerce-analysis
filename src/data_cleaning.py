import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def fill_missing_values(df):
    df = df.copy()
    df['city'] = df['city'].fillna('Unknown')
    df['unit_price'] = df['unit_price'].fillna(df['unit_price'].mean())
    return df

def remove_duplicates(df):
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset='order_id', keep='first')
    return df

def clean_strings(df):
    df = df.copy()
    df['city'] = df['city'].str.strip().str.title()
    df['city'] = df['city'].replace(
        to_replace=r'(?i)^casa.*',
        value='Casablanca',
        regex=True
    )
    return df

def convert_dates(df):
    df = df.copy()
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['ship_date'] = pd.to_datetime(df['ship_date'])
    return df
