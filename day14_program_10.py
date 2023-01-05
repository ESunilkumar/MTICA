''' hybrid inheritence class c is derived from class a and class b'''
class A:
    def first_method(self):
        print("method of a class a ......")
class B(A):
    def first_method(self):
        print("method of a class b ......")
        super().first_method()

ob=B()
ob.first_method()
    
