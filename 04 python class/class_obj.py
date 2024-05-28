

# pyhton class and objects

class car :

    # class variable
    wheel = 4

    # constructor
    def __init__(self, brand, model) :

        # instance variables
        self.brand = brand
        self.model = model

    # instance method:

    def display(self):
        print(f"{self.brand} {self.model} also has {self.wheel} wheels")

# creating objects
car1 = car("toyota","supra")    
car2 = car("mahindra","Thar")

# accessing instance variable and calling method
car1.display()      
car2.display()        

