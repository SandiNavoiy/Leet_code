import pandas as pd

gdp_usa = [
    31837000000,
    643000000,
    46607000000,
    42078000000,
    19325000000,
]
period = [
    "2018",
    "2019",
    "2020",
    "2021",
    "2022",
]
s = pd.Series(data=gdp_usa, index=period)

print(s)
