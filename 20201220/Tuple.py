tuple = ( 'abcd' , 786 , 2.23 , 'xyz' , 70.2 ) #Len = 5
tinytuple = ( 123 , 'john' ) #Len = 2

print (tuple)
print (tuple[0])
print (tuple[2])
print (tuple[1:3])
print (tuple[2:])
print (tinytuple * 2)
print (tinytuple[0] * 2)
print (tinytuple[1] * 2)

#concat

print(tuple + tinytuple)
print(tuple[0] + ' ' + tuple[3])
print(tuple[0] + ' ' + tinytuple[1])
print(tuple[1] + tuple[2]) #Integers added in concat
# print(tuple[0] + tuple[1]) #Error

# tuple[0] = 'Sandeepa' # tuple is read only
# print(tuple)