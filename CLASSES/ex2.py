class Square_numbers:
    def __init__(self,number):
       self.number = number

    def square(self):
        return (self.number  **2)
   
       
p1 = Square_numbers(16)
print(p1.square())
        