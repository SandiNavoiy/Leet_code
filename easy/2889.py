import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """Изменение формы данных: поворот"""
    return weather.pivot(index='month', columns='city', values='temperature')



