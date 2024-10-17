# Напишите определение класса Password       


# Ниже код для проверки методов класса Password

class Password:
    def __init__(self, password):
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password
    @property
    def strength(self):
        if len(self.__password) < 8:
            return "Weak"
        elif len(self.__password) < 12:
            return "Medium"
        else:
            return "Strong"



pass_1 = Password("Alligator34")
assert pass_1.password == "Alligator34"
assert pass_1.strength == "Medium"
assert len(pass_1.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

pass_2 = Password("Alligator345678")
assert pass_2.password == "Alligator345678"
assert pass_2.strength == "Strong"
pass_1.password = "123"
assert pass_1.strength == "Weak"
assert len(pass_2.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

pass_3 = Password("345678")
assert pass_3.strength == "Weak"
print('Good')
assert len(pass_3.__dict__) == 1, 'У ЭК должен храниться только один атрибут'