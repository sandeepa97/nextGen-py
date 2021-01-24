try:
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    answer = num2/num1
    print(answer)
except:
    print("It's getting runtime error. Please check your inputs")
finally:
    print("This is final code")

# finally keyword is optional. 

def runCal():
    try:
        num1 = int(input("Enter Number 1: "))
        num2 = int(input("Enter Number 2: "))
        answer = num2/num1
        print(answer)
    except:
        print("It's getting runtime error. Please check your inputs")
    finally:
        print("This is final code")

runCal()





# count = 0
# for count in range(10):
#     try:
#         num1 = int(input("Enter Number 1: "))
#         num2 = int(input("Enter Number 2: "))
#         answer = num2/num1
#         print(answer)
#     except:
#         print("It's getting runtime error. Please check your inputs")
