import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    new_emp = employees.assign(salary=employees["salary"] * 2)
    return new_emp


data = pd.DataFrame(
    {
        "name": ["Jack", "Piper", "Mia", "Ulysses"],
        "salary": [19666, 74754, 62509, 54866],
    }
)

new_temp = modifySalaryColumn(data)
print(f'"{new_temp}"')
