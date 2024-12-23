import os
import stat


def get_permissions(path: str):
    x = os.stat(path).st_mode
    return stat.filemode(x)[1:]


print(get_permissions("00.py"))
