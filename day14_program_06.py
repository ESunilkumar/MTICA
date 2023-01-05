class Wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print('grr...')
class Dog(Wolf):
    def bark(self):
        print("woof")

pet1=Dog("junnu","yellow")
pet1.bark()
pet2=Wolf("chinnu","orange")
pet2.bark()
Dog("acd","jkh").bark()
