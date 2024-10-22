from time import time


class Timer:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        start = time()
        self.fn(*args, **kwargs)
        end = time()
        print(f"Execution time: {end - start} seconds")


@Timer
def calculate():
    for i in range(10000000):
        2**100


calculate()
