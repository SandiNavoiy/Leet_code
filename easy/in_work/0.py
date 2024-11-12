class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(f"Point(x={self.x},y={self.y})")


p1 = Point(2, 5)

print(p1)
