# Basic class example
class Car:
    # Overwrites the default init, adding arguments and instance variable assignment
    def __init__(self, color, model='Toyota'):
        self.color = color
        self.model = model
        self.engine = "off"
    # Basic instance methods
    def start_engine(self):
        if self.engine == 'off':
            print("Starting the engine")
            self.engine = 'on'
        else:
            print("The engine is already running")
    def stop_engine(self):
        if self.engine == 'on':
            print("Stopping the engine")
            self.engine = 'off'
        else:
            print("The engine is already off")
    def drive(self):
        if self.engine == 'on':
            print("Driving the car")
        else:
            print("The engine needs to be started first")

    def display_car(self):
        print("The car is painted ", self.color)
        print("The car model is", self.model)
        print("The engine is ", self.engine)

# Class instance instantiation
my_car = Car("Blue")
other_car = Car("Red", "Honda Civic")
my_car.display_car()
my_car.drive()
other_car.start_engine()
other_car.display_car()
other_car.drive()
other_car.stop_engine()
other_car.display_car()

# Inheriting class
class HondaCivic(Car):
    def __init__(self, color):
        super().__init__(color, 'Honda Civic')