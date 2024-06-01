class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year


    def car1(self):
        print("Hello, my car make is", self.make, ", model is", self.model, ", and it's from the year", self.year)
      

p1 = car("Honda","civic" ,2020)
print(p1.car1())