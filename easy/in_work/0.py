class Car:
    model = "BMW"
    engine = 1.6

    @staticmethod
    def drive():
        print("Let's go")


a = Car()
b = Car()
Car.drive()
getattr(Car, "drive")()
# a.drive()
# b.drive()
