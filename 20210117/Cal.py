#Lecturer's code


n1 = int(input("Enter Number 01: "))
n2 = int(input("Enter Number 02: "))
operator = input("Enter Operator: ")

def add():
    result = n1 + n2
    print(result)
def sub():
    result = n1 + n2
    print(result)
def multi():
    result = n1 + n2
    print(result)
def div():
    result = n1 + n2
    print(result)

if operator == "+" :
    add()
elif operator == "-" :
    sub()
elif operator == "*":
    multi()
elif operator == "/":
    div()
else:
    print ("Invalid Operator")

