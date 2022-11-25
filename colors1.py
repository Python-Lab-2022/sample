list=[]
list1=[]
a=[]
n=int(input("enter the number of elements in list:"))
for i in range(0,n):
    list.append(str(input()))
n1=int(input("enter the no of elements in list1:"))
for i in range(0,n1):
    list1.append(str(input()))
for i in list:
    if i not in list1:
        a.append(i)
print (a)
