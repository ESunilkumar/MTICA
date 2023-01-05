class Dog:
    price=400
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def bark(self):
        print('Woof')
        print(self.name,"has" ,self.price,"and price and its color is",self.price)
if __name__=="__main__":
    pet1=Dog("Junnu","yellow")
    pet2=Dog("Chinnu","orange")
    pet1.bark()
    pet2.bark()
    print(pet1.price)
    print(pet2.price)
    print(Dog.price)
    Dog('vdf','greenn').bark()
        
