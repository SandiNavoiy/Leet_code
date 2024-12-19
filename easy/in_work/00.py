class Descriptor:

    def __set__(self, instance, value):
        instance._value = value

    def __get__(self, instance, owner):
        return instance._value


class Student:
    name = Descriptor()
    marks = Descriptor()


misha = Student()

misha.marks = [3, 4, 5]
misha.name = 'Михалыч'

print(misha.marks)
print(misha.name)