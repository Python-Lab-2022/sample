d={1:2,2:3,3:4,4:5,5:6,6:7}
print('Original dictionary : ',d)
sorted_d=sorted(d.items())
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d=dict(sorted(d.items()))
print('Dictionary in descending order by value : ',sorted_d)
