def add(num1, num2):
    result = num1 + num2
    return result
def sub(num1, num2):
    result = num1 - num2
    return result
def multi(num1, num2):
    result = num1 * num2
    return result
def div(num1, num2):
    result = num1 / num2
    return result

def runCal():
    n1 = int(input("Enter Number 01: "))
    n2 = int(input("Enter Number 02: "))
    operator = input("Enter Operator: ")

    if operator == "+" :
        r = add(n1, n2)
        print(r)
    elif operator == "-" :
        r = sub(n1, n2)
        print(r)
    elif operator == "*":
        r = multi(n1, n2)
        print(r)
    elif operator == "/":
        r = div(n1, n2)
        print(r)
    else:
        print ("Invalid Operator")

runCal()

