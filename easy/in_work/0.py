a =int(input())
if a<2:
    print("Младенец")
if a>=2 and a<4:
    print("Малыш")
elif a>=4 and a<12:
    print("Ребёнок")
elif a>=12 and a<19:
    print("Подросток")
elif a>=19 and a<65:
    print("Взрослый человек")
elif a>=65 and a<1000:
    print("Пожилой человек")
