class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move")

class Car(Vehicle):
   ''' def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")'''

class Boat(Vehicle):
   ''' def __init__(self, brand, model):
        self.brand = brand
        self.model = model'''

    def move(self):
        print("Sail")

class Plane(Vehicle):
    '''def __init__(self, brand, model):
        self.brand = brand
        self.model = model'''

    def move(self):
        print("Fly")

car1 = Car("Toyota","Camry")
boat1 = Boat("Yamaha","242X")
plane1 = Plane("Boeing","747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()