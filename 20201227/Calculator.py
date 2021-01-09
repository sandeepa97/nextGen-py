num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
action = input("Enter Action: ")

if action == "+":
    print (num1 + num2)
elif action == "-":
    print (num1 - num2)
elif action == "*":
    print (num1 * num2)
elif action == "/":
    print (num1 / num2)
else:
    print ("Wrong Operator")