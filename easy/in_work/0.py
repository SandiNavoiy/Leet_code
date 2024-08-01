def speller(param):
    if len(param) > 0:
        print(param[-1])
        speller(param[:-1])


speller("Artem")
