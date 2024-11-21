n = input()
count = 0

while count <= len(n):
    if n[count] == "a" or n[count] == "e":
        print("Ага! Нашлась")
        break
    else:
        print(f"Текущая буква: {n[count]}")

    count += 1
else:
    print("Распечатали все буквы")
