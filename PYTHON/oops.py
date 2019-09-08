import math
class Student():
    school = "Rashtrothana"
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        bmi = (self.weight/math.pow(self.height,2))
        if bmi < 25:
            return ("Slim")
        else:
            return ("Overweight")

shiva = Student("shiva",1.64,75)
print(shiva.name,shiva.height,shiva.weight)
print ("and BMI says: you are "+shiva.bmi())
