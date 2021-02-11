class Vehicle:

    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def accelerate(self):
        print("The car is accelerating")
        print("Car Model :" + self.model)
        print("Car Year :" + self.year)
    
    def brake(self):
        print("Brake is applied")

    def steerLeft(self):
        print("The Car is steering Left")

    def steerRight(self):
        print("The Car is steering Right")


bmw = Vehicle("model x" , "2016")
bmw.accelerate()
# audi = Vehicle()
# honda = Vehicle()