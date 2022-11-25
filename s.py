import operator
employees ={}
n=int(input("enter the number of elements:"))
for i in range(3):
    name=input("enter employee's name:")
    salary=input("enter employee's salary:")
    employees[name]=salary
print("dictionary",employees)
a=sorted(employees.items(),key=operator.itemgetter(1))
print('asscending order is',a)
d=dict(sorted(employees.items(),key=operator.itemgetter(1),reverse= True))
print('descending order is',d)
  
