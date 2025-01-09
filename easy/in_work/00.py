# pass = input()
pas = "qwerty"
n = 3
while True:
    new = input()
    n -= 1
    if new != pas:
        print("Введен неправильный пароль!")
        print(f"Лимит попыток = {n}")
    else:
        print("Вы ввели правильный пароль! Добро пожаловать!")
        break
    if n == 0:
        print("Вы потратили все свои попытки! Приходите завтра")
        break
