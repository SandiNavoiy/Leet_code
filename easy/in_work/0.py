def test(f):
    def www(*args):
        return f(*args) * 2
    return www


@test
def gggg(x):
    return x * 2



t= 2

print(gggg(t))