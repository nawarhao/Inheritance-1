class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

#Python code to demonstrate how parent constructors are called

#parent class
class Person(object):
    #__init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        
#child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        
        #invoking the __init__ of the parent class
        
        Person.__init__(self, name, idnumber)
        

#creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

#calling a function of the class Person using its instance
a.display()

#parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")
        
    def whoisThis(self):
        print("Bird")
        
    def swim(self):
        print("Swim faster")
        
# child class
class Penguin(Bird):
    
    def __init__(self):
        #call super() function
        super().__init__()
        print("Penguin is ready")
        
    def whoisThis(self):
        print("Penguin")
        
        
    def run(self):
        print("Run faster")
        

#object creation
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()