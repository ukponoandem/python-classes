#USING THE MAX FUNCTION

class maximum_number:
    def __init__(self ,number):
       self.number = number

    def maximum(self):
        return  max(self.number)
       

p1 = maximum_number([23,45,22,34,67,33,88])
print(p1.maximum())