class House:
    def __init__(self,storey,size):
        self.storey = storey
        self.size = size
    def makeFoundation(self):
        print("foundation")
        print("foundation Size: " + self.size)
        print("foundation Size: " + self.storey)
    def makeWalls(self):
        print("walls")
    def makeRoof(self):
        print("roof")


houseA = House(2, 10)
houseA.makeFoundation()


