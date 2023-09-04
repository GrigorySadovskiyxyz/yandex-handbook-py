import pandas as pd

data = pd.read_csv('2019.csv')
data = data.sort_values("Score", ascending=False)
print(list(data['Country or region'])[0:10])
