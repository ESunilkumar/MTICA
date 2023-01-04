def printsun():
    print('Sunday\n')
def printmon():
    print('Monday\n')
def printtue():
    print('Tuesday\n')
def printwed():
    print('Wednesday\n')

def printthu():
    print('Thursday\n')
def printfri():
    print("Friday\n")
def printsat():
    print("Saturday")

def choice():
    print("0:Sunday")
    print("1:Monday")
    print("2:Tuesday")
    print("3:Wednesday")
    print("4:Thursday")
    print("5:Friday")
    print("6:Saturday")
    print("7:Invalid")

select=0

daydict={0:printsun,1:printmon,2:printtue,3:printwed,4:printthu,5:printfri,6:printsat}
choice()
daynum=int(input("enter dayno:"))
if (daynum>=0)and (daynum<7):
                     daydict[daynum]()
else:
    print("INVALID")



