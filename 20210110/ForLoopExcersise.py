#01

fruitList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

for fruit in fruitList:
    print(fruit)


#02 => no C
fruitList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


tempList = [x for x in fruitList if x != "c"]
for fruit in tempList:
    print(fruit)


#03 => terminate before f

fruitList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

temp = fruitList.index("f") 
rest = fruitList[:temp] 

for fruit in rest:
    print(fruit)

