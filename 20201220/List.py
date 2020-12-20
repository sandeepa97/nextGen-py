list = [ 'abcd' , 786 , 2.23 , 'xyz' , 70.2 ] #Len = 5
tinylist = [ 123 , 'john' ] #Len = 2

print (list)
print (list[0])
print (list[2])
print (list[1:3])
print (list[2:])
print (tinylist * 2)
print (tinylist[0] * 2)
print (tinylist[1] * 2)

#concat

print(list + tinylist)
print(list[0] + ' ' + list[3])
print(list[0] + ' ' + tinylist[1])
print(list[1] + list[2]) #Integers added in concat
# print(list[0] + list[1]) #Error

list[0] = 'Sandeepa' # lists can be read and write
print(list)