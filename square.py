list1=[]
list2=[]
l=int(input("enter lower range:"))
u=int(input("enter upper range:"))
for i in range(l,u):
        list1.append(i)
for i in list1:
    if(i*i)%i==0:
        list2.append(i)
print(list2)
