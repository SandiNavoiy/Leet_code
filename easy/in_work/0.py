class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


user1 = User('batya99', 'admin')


class Access:

    __access_list= ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        if role in Access.__access_list:
            return True
        else:
            return False
    @staticmethod
    def get_access(user):
        if isinstance(user, User):
            if Access.__check_access(user.role):
                print(f"User {user.name}: success")
            else:
                print("AccessDenied")
        else:
            print("AccessTypeError")


Access.get_access(user1) # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied

Access.get_access(5) # печатает AccessTypeError