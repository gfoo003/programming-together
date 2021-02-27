studentInput=input("2+2=")
x=0
try:
    x=float(studentInput)
except:
    print("That's not a number, try again!")
    #remember to assign back the same variable
    x=input("2+2=")
    while x!=2+2:
        print("That's not a number, try again!")
        x=input("2+2=")
while x!=2+2:
    print("Try again!")
    x=input("2+2=")
    x=float(x)
print("Genius")
print("End")