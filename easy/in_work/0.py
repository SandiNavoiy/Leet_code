class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value.upper()

    name = property(get_name, set_name)


student = Student(name="Kevin")
print(student.name)
student.name = "Kev"
print(student.name)
