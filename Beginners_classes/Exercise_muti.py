class number_multipy:
      def __init__(self,multiplication,mutiply):
        self.multiplication = multiplication
        self.multipy = mutiply

      def my_multiplication(self):
       return (self.multiplication * self.multipy)

p1 = number_multipy(3,3)
print(p1.my_multiplication())