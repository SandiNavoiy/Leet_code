from datetime import datetime, timedelta

# Ввод даты от пользователя
input_date_str = input()

# Преобразование строки в объект даты
input_date = datetime.strptime(input_date_str, "%m/%d/%Y")
for i in range(15):
    input_date += timedelta(days=1)  # Следующий день
    print(input_date.strftime("%d-%m-%Y"))
# Вычисление дат
