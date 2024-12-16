from collections import UserDict

# Напишите определение класса ContactBook


class ContactBook:
    def __init__(self):
        self.data = UserDict()

    def add_contact(self, k, v):
        if k in self.data:
            print(f"Контакт {k} уже существует")
        else:
            self.data[k] = v
            print(f"Контакт {k} создан")

    def __getitem__(self, item):
        return self.data[item]

    def display_contacts(self):
        for k, v in self.data.items():
            print(f"{k}: {v}")

    def update_contact(self, k, v):
        if k in self.data:
            self.data[k] = v

        else:
            print(f"Контакт {k} не найден")

    def delete_contact(self, k):
        if k in self.data:
            del self.data[k]
            print(f"Контакт {k} удален")
        else:
            print(f"Контакт {k} не найден")


contact_book = ContactBook()
contact_book.add_contact("John", "123-456-7890")
assert contact_book.data["John"] == "123-456-7890"
contact_book.add_contact("John", "345-666")  # Печатает Контакт John уже существует.
contact_book.add_contact("Alice", "987-654-3210")
assert contact_book.data["Alice"] == "987-654-3210"
contact_book.display_contacts()
#
contact_book.update_contact("John", "111-222-3333")
assert contact_book.data["John"] == "111-222-3333"
contact_book.display_contacts()

contact_book.delete_contact("Alice")
assert "Alice" not in contact_book.data
contact_book.display_contacts()
