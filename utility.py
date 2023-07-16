import pandas as pd

def get_golden_cross(data, fast_ma, slow_ma):
    df = pd.DataFrame(data, index=data.index)
    df['fast_ma'] = data.rolling(fast_ma).mean()
    df['slow_ma'] = data.rolling(slow_ma).mean()

    df = df.dropna()

    series1 = df['fast_ma'] < df['slow_ma']
    series2 = df['fast_ma'] >= df['slow_ma']

    golden_cross = df[~(series1 | series2.shift(1))].index    

    return golden_cross


def get_death_cross(data, fast_ma, slow_ma):
    df = pd.DataFrame(data, index=data.index)
    df['fast_ma'] = data.rolling(fast_ma).mean()
    df['slow_ma'] = data.rolling(slow_ma).mean()

    df = df.dropna()

    series1 = df['fast_ma'] < df['slow_ma']
    series2 = df['fast_ma'] >= df['slow_ma']

    death_cross = df[series1 & series2.shift(1)].index   

    return death_cross
    

def add_avg_price(data):
    data['Avg'] = (data['Open'] + data['Close']) / 2
    return data

def get_days_duration(data):
    d1 = pd.to_datetime(data.index[0])
    d2 = pd.to_datetime(data.index[-1])
    diff = d2 - d1
    return diff.days

def get_years_duration(data):
    days = get_days_duration(data)
    return (days/365)
