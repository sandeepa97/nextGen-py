def add(num1, num2):
    result = num1 + num2
    print(result)
def sub(num1, num2):
    result = num1 - num2
    print(result)
def multi(num1, num2):
    result = num1 * num2
    print(result)
def div(num1, num2):
    result = num1 / num2
    print(result)

def runCal():
    n1 = int(input("Enter Number 01: "))
    n2 = int(input("Enter Number 02: "))
    operator = input("Enter Operator: ")

    if operator == "+" :
        add(n1, n2)
    elif operator == "-" :
        sub(n1, n2)
    elif operator == "*":
        multi(n1, n2)
    elif operator == "/":
        div(n1, n2)
    else:
        print ("Invalid Operator")

runCal()

# NOTE
# Parameters act as local Variables