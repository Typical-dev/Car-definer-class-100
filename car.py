class Car(object):
    def __init__(self, model, color, company, speedLimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedLimit = speedLimit
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerating")
    def changeGear(self):
        print("gearChanged")


lamborghini = Car("Diablo SV", "red", "lamborghini", "250")
print(lamborghini.speedLimit)