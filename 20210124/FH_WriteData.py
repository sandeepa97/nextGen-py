import os


def appendTextFile():
    fileName = open("Animal.txt", "a")
    fileName.write("\nHuman")
    fileName.close()

def writeTextFile():
    fileName = open("Animal.txt", "w")
    fileName.write("All animals are human")
    fileName.close()

def createTextFile():
    fileName = open("NewFile.txt", "x")

def deleteTextFile():
    # os.remove("NewFile.txt")
    os.rmdir("test")

deleteTextFile()