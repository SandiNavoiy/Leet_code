# Названия дней недели
days_of_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

# Создаем генераторное выражение
days = ((day_number, days_of_week[(day_number - 1) % 7]) for day_number in range(1, 78))

# Печатаем первые 77 дней
for day in days:
    print(day)
