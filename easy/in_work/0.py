def is_dunder(param):
    if len(param) < 6:
        return False
    s1= param[:2]
    s3= param[-2:]
    s2 = param[2:-2]
    if s1 != "__":
        return False
    if s3 != "__":
        return False
    if s2.count("_") != 0:
        return False
    if len(s2) < 2:
        return False
    if not s2.isalpha():
        return False



    return True


assert is_dunder('__str__') == True
assert is_dunder('___bool___') == False
assert is_dunder('__s__') == False
assert is_dunder('__abvc3__') == False
assert is_dunder('____') == False
assert is_dunder('_str__') == False
assert is_dunder('__str_') == False
assert is_dunder('__ab__') == True
#
# print('test is ok')

