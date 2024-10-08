def replace(text, old, new=""):
    ee = ""
    for i in text:
        if i == old:
            ee += new
        else:
            ee += i
    return ee


print(replace("Bella Ciao", "a"))
