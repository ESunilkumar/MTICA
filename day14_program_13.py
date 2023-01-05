class Employee:
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount += 1
    def displaycount(self):
        print("total employee:",Employee.empcount)
    def displayEmployee(self):
        print("name:",self.name,"salary",self.salary)
emp1=Employee("sunilk:",2344447)
print("total employees:",Employee.empcount)
emp2=Employee("kamalk:",44774447)
emp1.displayEmployee()
emp2.displayEmployee()
print("total employees {0}".format(Employee.empcount))
emp3=Employee("kumark:",44447)
emp3.displaycount()
emp2.displaycount()
emp1.displaycount()
print("total employees {0}".format(Employee.empcount))
