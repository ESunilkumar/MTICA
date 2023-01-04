def printadd(a,b):
    return a+b
def printsub(a,b):
    return a-b
def printmul(a,b):
    return a*b
def printdiv(a,b):
    return a/b

def choice():
    print("+:addition")
    print("-:substraction")
    print("*:multiplication")
    print("/:division")
    return 


colorselect={"+":printadd,"-":printsub,"*":printmul,"/":printdiv}
while True:
    choice()
    selection=input("select arthematic operation d")
    if(selection=='q' or selection=='Q'):break
    if(selection=='+') or (selection=='-') or (selection=='*') or (selection=='/'):
        n1=int(input("enter a"))
        n2=int(input("enter a"))
        z=colorselect[selection](n1,n2)
        print(n1,selection,n2,'=',z)
