rows = int(input("enter a number"))
for i in range(0, rows):
    for j in range(0, rows-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")
