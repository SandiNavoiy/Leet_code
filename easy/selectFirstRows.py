import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """Отображение первых трех строчек pandas"""

    return employees.head(3)



data = pd.DataFrame({
    "employee_id": [3, 90, 9, 60, 49, 43],
    "name": ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    "department ": ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    "salary": [48675, 11096, 33805, 37678, 23793, 40454],
}
)

print(selectFirstRows(data))
