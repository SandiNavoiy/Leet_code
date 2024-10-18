class MyClass:
    class_attribute = "I am a class attribute"

    @staticmethod
    def change(new_value):
        MyClass.class_attribute = new_value


example_1 = MyClass()
example_2 = MyClass()

example_1.change("Class attribute modified")

print(example_1.class_attribute)
print(example_2.class_attribute)
