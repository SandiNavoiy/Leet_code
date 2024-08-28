def is_member(param, lst):
    if len(lst) >0:
        if param == lst[0]:
            return True
        else:
            return is_member(param, lst[1:])

    return False


print(is_member("e", ['a', 'e', 'i', 'o', 'u']))