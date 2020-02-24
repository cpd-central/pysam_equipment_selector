import pandas as pd

df = pd.read_csv('12x24_rates.csv', header=None)

df.columns = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
]

df = df.T

df.to_csv('12x24_rates_cleaned.csv')
