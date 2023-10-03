class BaseClass:

    def __init__(self):
        print("Base init")

    def set_name(self, name):
        self.name = name
        print("base class set name")


class SubClass(BaseClass):

    def __init__(self):
        super().__init__()
        print("sub init")

    def welcome(self):
        print("welcome")

    def set_name(self, name):
        super().set_name(name)
        print("sub class set name")

    def display_name(self):
        print("name :" + self.name)


y = SubClass()
y.welcome()
y.set_name("kadeeja")
y.display_name()
