class Vehicle:
    def __init__(self,name,max_speed,milege):
        self.name=name
        self.max_speed=max_speed
        self.milege=milege

    def seating_capacity(self,capacity):
        return f"the seating capacity of a {self.name}\
     is (capacity) passengers"
class Bus(Vehicle):
     def seating_capacity(self,capacity=50):
         return super().seating_capacity(capacity=50)


school_bus=Bus("school volvo",180,207)
print(school_bus.seating_capacity())
