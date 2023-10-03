number = int(input("Enter the number of which multiplication table should be printed"))
limit = int(input("Enter the number upto which multiplication table should be printed"))
for i in range(1, limit+1):
    res=i*number
    print(str(i)+" * "+str(number)+" = "+str(res))