class Cat:
    def __init__(self,color,legs):
        self.color=color
        self.legs=legs
    def __str__(self):
        temp='cat is'+self.color+'color is'+'and has'+str(self.legs)
        return temp
if __name__=="__main__":
    pet1=Cat("ginger4",4)
    print(pet1.color)
    print(pet1.legs)
    print(pet1)

    pet2=Cat("brown",7)
    print(pet2.legs)
    print(pet2.color)
    print(pet2)
