import datetime

current_time = datetime.datetime.now()


print("current year is:" , current_time .year)
last=int(input("enter the lastyear "))
print("leap years are:")
for year in range(current_time.year,last):
    if(year%400==0) and (year%100==0):
        print(year)
    if(year%4==0) and (year%100!=0):
        print(year)



