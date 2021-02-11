class Vehicle:
    def start(self):
        print("Vehicle is starting....")

    def changeGear(self):
        print("Changing Vehicle Gear....")


class Car(Vehicle):

    def __init__(self):
        print("This is car constructor")

    def autoPark(self):
        print("Car is automatically parking")
    
    def start(self):
        print("This is car starting method. I am starting using Push Button!")

class Bus(Vehicle):

    def __init__(self):
        print("this is bus constructor")

class Jeep(Vehicle):

    def __init__(self):
        print("this is jeep constructor")


class Sedan(Car):
    
    def __init__(self):
        print("this is sedan car constructor")

    def start(self):
        print("this is sedan car start. i am using Sensors to start!")

vitz = Car()
vitz.start()
vitz.changeGear()

tata = Bus()
tata.start()

premio = Sedan()
premio.start()


# vitz.changeGear()
# vitz.autoPark()

# vehicleObj = Vehicle()
# vehicleObj.changeGear()


# premio = Sedan()
# premio.autoPark()