
#example 1
h_letters = [ letter for letter in 'human' ]
print( h_letters)

#example 2
list_x = [x*2 for x in range(5)] # returns [0,2,4,6,8]
print(list_x)

#example 3:
l1 = [100,200,300]
l2 = [0,1,2]

#example 4:
list_y = [x + y for x in l2 for y in l1 ]
print("List y:", list_y)
#example 5:
list_yy = [x * y for x in l2 for y in l1 ]
print("List yy:", list_yy)


list_a = [1,2,3]
list_b = [3,4,5]
list_c = [list_a,list_b]
print("List cc original :", list_c)

#example 6:
list_xx = [y*y for x in list_c for y in x]
list_c1 = [item*item for x in list_c for count,item in enumerate(x) ]
print("List xx:", list_xx)
print("List c1:", list_c1)

for each_list in list_c:
    for count,item in enumerate(each_list):
        each_list[count] = item*item

print("List cc:", list_c)

h_letters = [ letter for letter in 'human' ]
print( h_letters)

#Enumerate
a = [1, 2, 3, 4]
aa = [ i*n for i,n in enumerate(a)]
print(aa)