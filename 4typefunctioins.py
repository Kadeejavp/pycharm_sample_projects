def sum1():
    num1=1
    num2=2
    sum=num1+num2
    print(sum)

def sum2(num1,num2):
    sum= num1+num2
    print(sum)

def sum3():
    num1=1
    num2=2
    sum=num1+num2
    return sum

def sum4(num1,num2):
    sum=num1+num2
    return sum

sum1()
sum2(1,2)
result3=sum3()
print(result3)
result4=sum4(1,2)
print(result4)