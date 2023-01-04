def printblue():
    print('you chose is blue!\n')
def printred():
    print('you chose is red!\n')
def printorange():
    print('you chose is orange!\n')
def printyellow():
    print('you chose is yellow!\n')
def choice():
    print("0:blue")
    print("1:red")
    print("2:orange")
    print("3:yellow")
    print("4:quit")
    return
colorselect={0:printblue,1:printred,2:printorange,3:printyellow}
selection=0
while True:
    if selection==4:break
    choice()
    selection=int(input("select color option"))
    if(selection>=0) and (selection<4):
        colorselect[selection]()
