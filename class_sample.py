class CrossroadsTeam:
    year=2023
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def add_age(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place=place

    def display(self):
        print("year :"+str(CrossroadsTeam.year))
        print("name :"+self.name)
        print("age :"+str(self.age))
        print("place :"+self.place)

    @classmethod
    def add_year(cls):
        cls.year=cls.year+1

    @staticmethod
    def display_welcome():
        print("welcome")


CrossroadsTeam.display_welcome()

x=CrossroadsTeam("nikhil",37,"calicut")
y=CrossroadsTeam("dilshad",24,"malappuram")

x.display()
y.display()

print("------------")

CrossroadsTeam.year=CrossroadsTeam.year+1
x.add_age()
y.add_age()
x.display()
y.display()

print("------------")

CrossroadsTeam.add_year()
x.add_age()
y.add_age()
x.relocate("delhi")
y.relocate("mumbai")
x.display()
y.display()




