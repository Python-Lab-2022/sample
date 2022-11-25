

color_list_1  = ['blue','red','white','violet']    
color_list_2 = ['white','blue','yellow','green']    
a = set(color_list_1 + color_list_2)          
for n in a:        
if  n in color_list_2:            
c = set(a - set(color_list_2))              
return c
