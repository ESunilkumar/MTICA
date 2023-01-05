''' hybrid inheritence class c is derived from class a and class b'''
class A:
    def first_method(self):
        print("method of a class a ......")
class B:
    def first_method(self):
        
        print("method of a class b ......")
class C(A,B):#B,A
    def third_method(self):
        
        print("method of a class  c ......")


if __name__=="__main__":
    ob=C()
    ob.first_method()
    ob. third_method()
    '.'
    
