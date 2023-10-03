def hey(name):
    print("my name is "+name)

#value=input("Enter your name")
#hey(value)

def hello(*words):
    print("first word is "+words[0]+" second word is "+words[1])

#hello("hey","hello")

value=10

def hoi():
    value=30
    print(value)

print(value)
hoi()