import pandas as pd

data = {'name ': ["A", "B", "C", "D"], 'sex ': ["m", "f", "m", "f"], "salary": [2500, 1500, 1000, 500]}
df = pd.DataFrame(data)

df = df.replace(["m", "f"], ["f", "m"])
