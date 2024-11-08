class Student:
    def __init__(self, name):
        self.name = name
        self._course = 1
        self.__marks = []


student = Student(name="Kevin")
print(student.__dict__)
