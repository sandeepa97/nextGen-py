#Self Developed code

def add(num1,num2):
    result = num1 + num2
    print("Addition : ",result)

def sub(num1,num2):
    result = num1 - num2
    print("Subtraction : ",result)

def multi(num1,num2):
    result = num1 * num2
    print("Multiplication : ",result) 

def div(num1,num2):
    result = num1 / num2
    print("Division : ",result)


num1=int(input("Enter number one: "))
num2=int(input("Enter number two :"))
operator=input("Enter operator : ")

if operator == "+" :
    add(num1,num2)
elif operator == "-" :
    sub(num1,num2)
elif operator == "*":
    multi(num1,num2)
elif operator == "/":
    div(num1,num2)
else:
    print ("Invalid Operator")


