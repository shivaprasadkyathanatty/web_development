class Human():
    def __init__(self):
        print ("I am a Human")

class Boy(Human):
    def __init__(self,name):
        Human.__init__(self)
        self.name=name

    def __str__(self):
        return ("My Name is: {}".format(self.name))

class Girl(Human):
    def __init__(self,name):
        Human.__init__(self)
        self.name=name

    def __str__(self):
        return ("My Name is: {}".format(self.name))

shiva=Boy("shiva")
print (shiva)
asha=Girl("asha")
print (asha)
