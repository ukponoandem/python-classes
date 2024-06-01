class person:
    def __init__(self,name,age,subject):
        self.name = name
        self.age = age
        self.subject = subject


    def my_name(self):
        print("Hello my name is ", self.name,"and am ", self.age, "years old ", self.subject)
      

p1 = person("Ukpono",23 ,"mathematics")
print(p1.my_name())