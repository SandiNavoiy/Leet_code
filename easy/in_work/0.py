class PrettyPrint:
    def __str__(self):
        return f"{self.__class__.__name__}({', '.join([f'{i}={self.__dict__[i]}' for i in self.__dict__])})"


class Student(PrettyPrint):
    def __init__(self, name, surname, student_id, faculty, specialty):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.specialty = specialty

    def __str__(self):
        return f"{self.name} {self.surname}"


student_1 = Student("Иван", "Иванов", 12345, "Физический", "Математика")
student_2 = Student("Анна", "Смирнова", 67890, "Химический", "Биология")
print(student_1)
print(student_2)
