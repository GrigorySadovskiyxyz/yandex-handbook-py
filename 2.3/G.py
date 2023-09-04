import pandas as pd

data = pd.read_csv('2019.csv')
print(sum(list(data['GDP per capita'])))
