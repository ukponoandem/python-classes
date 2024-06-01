class Height_number:
    def __init__(self ,number1):
        self.number1 = number1

    def maximum_number(self): 
     height = 0
     for num in self.number1:
         if num > height:
           height = num
     return height
p1 = Height_number([12,23,45,56,66,77])
print(p1.maximum_number())