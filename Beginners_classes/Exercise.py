class Animals:
    def __init__(self,name ,species) :
          self.name = name
          self.sepcies = species

    def favorites(self):
          return ("Woof! Woof!")
          

class Dogs(Animals):
     def __init__(self, name, species):
          super().__init__(name, species)

p1 = Dogs("Max","Bulldog")
print(p1.favorites())
