class First:
    def display(self):
        print("first")
class Second:
    def display(self):
        print("second")

class Third(First,Second):
    def display_third(self):
        print("third")

x=Third()
x.display_third()
x.display()

print(Third.mro())