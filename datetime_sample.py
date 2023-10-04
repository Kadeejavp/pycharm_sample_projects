import datetime

now=datetime.datetime.now()

print(now.strftime("%d/%m/%Y"))

print(datetime.date.today())

x=datetime.datetime(2023,4,24,)
y=datetime.datetime(2023,5,27)

dif=x-y
print(dif)

end=datetime.datetime.now()
diff=end-now
print(diff)