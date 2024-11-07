# Напишите определение класса File
class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def remove(self):
        print(f"Файл {self.name} был удален")
        self.is_deleted = True

    def restore_from_trash(self):
        print(f"Файл {self.name} восстановлен из корзины")
        self.in_trash = False

    def read(self):
        if self.is_deleted:
            print(f"ErrorReadFileDeleted({self.name})")
            return
        elif self.in_trash:
            print(f"ErrorReadFileTrashed({self.name})")
            return

        else:
            print(f"Прочитали все содержимое файла {self.name}")

    def write(self, content):
        if self.is_deleted:
            print(f"ErrorWriteFileDeleted({self.name})")
            return
        elif self.in_trash:
            print(f"ErrorWriteFileTrashed({self.name})")
            return

        else:
            print(f"Записали значение {content} в файл {self.name}")


class Trash:
    content = []

    @staticmethod
    def add(file):
        if not isinstance(file, File):
            print(f"В корзину можно добавлять только файл")
        else:
            Trash.content.append(file)
            file.in_trash = True

    @staticmethod
    def restore():
        print(f"Восстанавливаем файлы из корзины")
        for file in Trash.content:
            file.restore_from_trash()
        Trash.content = []
        print(f"Корзина пуста")

    @staticmethod
    def clear():
        print(f"Очищаем корзину")
        for file in Trash.content:
            file.remove()
        Trash.content = []
        print(f"Корзина пуста")


# Ниже код для проверки класса File
f1 = File("puppies.jpg")
f2 = File("cat.jpg")
f3 = File("xxx.doc")
passwords = File("pass.txt")

for file in [f1, f2, f3, passwords]:
    assert file.is_deleted is False
    assert file.in_trash is False

f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.write("hello")
#
assert Trash.content == []
#
Trash.add(f2)
Trash.add(passwords)
Trash.add(f3)
#
f1.read()
Trash.add(f1)
f1.read()
#
for file in [f1, f2, f3, passwords]:
    assert file.in_trash is True
#
for f in [f2, passwords, f3, f1]:
    assert f in Trash.content
#
Trash.restore()
assert Trash.content == [], "После восстановления корзина должна была очиститься"
#
Trash.add(passwords)
Trash.add(f2)
Trash.add("hello")
Trash.add(f1)
#
for f in [passwords, f2, f1]:
    assert f in Trash.content
#

Trash.clear()
#
for file in [passwords, f2, f1]:
    assert file.is_deleted is True
#
assert Trash.content == [], "После удаления файлов корзина должна была очиститься"
#
f1.read()
