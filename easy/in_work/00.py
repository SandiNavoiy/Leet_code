def unical_word(file_name: str) -> int:
    with open(f"{file_name}", "r", encoding="utf-8") as f:
        s = []

        for i in f:
            for j in i.split():
                if j.lower() not in s:
                    s.append(j.lower())

                else:
                    continue

    return print(len(s))


unical_word("lorem.txt")
