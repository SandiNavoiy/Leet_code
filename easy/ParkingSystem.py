class ParkingSystem:
    """Модель парковки"""

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big = self.big -1

                return True
            else:
                return False

        elif carType == 2:
            if self.medium > 0:
                self.medium = self.medium - 1
                return True
            else:
                return False

        elif carType == 3:
            if self.small > 0:
                self.small = self.small - 1
                return True
            else:
                return False





obj = ParkingSystem(1, 1, 0)
param_1 = obj.addCar(3)
print(param_1)