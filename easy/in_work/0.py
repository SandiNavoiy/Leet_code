def digital_root(param):
    if len(str(param)) == 1:
        return param
    else:
        return digital_root


root = digital_root(9999999)
print(root)
9
