def openNameListFile():
    try:
        # fileName = open("D:\\Python\\Exercises\\common\\Namelist.txt", "r") 
        #above code for file path
        fileName = open("Namelist.txt", "r")
        print(fileName.read())
    except:
        print("File can not find in the location!")

def openNameListFileCharacters():
    try:
        fileName = open("D:\\Python\\Exercises\\common\\Namelist.txt", "r") 
        print(fileName.read(19))
    except:
        print("File can not find in the location!")

def openNameListFileLines():
    try:
        fileName = open("D:\\Python\\Exercises\\common\\Namelist.txt", "r") 
        print(fileName.readline())
        print(fileName.readline())
        print(fileName.readline())
    except:
        print("File can not find in the location!")

openNameListFile()
openNameListFileCharacters()
openNameListFileLines()


