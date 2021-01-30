def readFileUsingLoop():
    try:
        fileName = open("D:\\Python\\Exercises\\common\\Namelist.txt", "r")

        for f in fileName:
            print(f)

        fileName.close()

    except:
        print("File can not find in the location!")


readFileUsingLoop()