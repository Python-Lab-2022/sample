list= [10,20,30,40]

print("original list:")
print(list)
for i in list:
     if(i%2==0):
         list.remove(i)
print("list after removing EVEN numbers:")
print (list)
