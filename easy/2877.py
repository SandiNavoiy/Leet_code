import pandas as pd


def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    """Создать DataFrame из списка"""
    w = []
    q = []
    for i in student_data:
        w.append(i[0])
        q.append(i[1])
    data = {"student_id": w, "age": q}

    return pd.DataFrame(data)


student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]
print(createDataframe(student_data))
# data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
