import math
import random


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> list[float]:
        # Случайный угол
        angle = random.uniform(0, 2 * math.pi)
        # Случайное расстояние от центра (с учетом плотности распределения)
        distance = math.sqrt(random.uniform(0, 1)) * self.radius
        # Вычисление координат
        x = self.x_center + distance * math.cos(angle)
        y = self.y_center + distance * math.sin(angle)
        return [x, y]


# Your Solution object will be instantiated and called as such:
radius = 10.0
x_center = 5.0
y_center = -7.5
obj = Solution(radius, x_center, y_center)
param_1 = obj.randPoint()
print(param_1)