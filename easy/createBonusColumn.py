import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """Добавление столбца в pandas"""
    employees_new = employees.assign(bonus=employees["salary"] * 2)

    return employees_new


data = pd.DataFrame(
    {
        "name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas"],
        "salary": [4548, 28150, 1103, 6593, 74576, 24433],
    }
)


print(createBonusColumn(data))
