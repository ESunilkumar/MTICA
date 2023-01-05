''' indirect inheritence or mutilevel inheritence'''
class A:
    def first_method(self):
        print("method of a classa ......")
class B(A):
    def second_method(self):
        
        print("method of a classb ......")
class C(B):
    def third_method(self):
        
        print("method of a classc ......")


if __name__=="__main__":
    ob=C()
    ob.first_method()
    ob.second_method()
    ob. third_method()
    obj=B()
    obj.third_method()
        
