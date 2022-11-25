list=[]
c=0
n=int(input("Enter the no of names"))
for i in range(0,n):
    list.append(input()) 
print(list)
for i in list:
    for j in i:
       if j=='a':
          c=c+1
print(c)
    
