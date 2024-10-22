import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """"""
    t = customers.drop_duplicates(subset=["email"])
    return t


q = pd.DataFrame(
    {
        "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
        "email": [
            "emily@example.com",
            "michael@example.com",
            "sarah@example.com  ",
            "john@example.com",
            "john@example.com",
            "alice@example.com",
        ],
    }
)

print(dropDuplicateEmails(q))
