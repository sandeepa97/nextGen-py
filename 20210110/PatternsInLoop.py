#print a pyramid with 9 rows 

m = (2 * 10) - 2
for i in range(0, 10):
    for j in range(0, m):
        print(end=" ")
    m = m - 1  # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("*", end=' ')
    print(" ")

# loopList = ["*"]
# count = 0
# for x in loopList:
#     while (count < 5):
#        count = count + 1 
#        print(x)
#        x=x+x