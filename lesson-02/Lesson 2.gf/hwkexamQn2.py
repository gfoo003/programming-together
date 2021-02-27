studentInput=input("2+2=")
x=studentInput
try:
    x=float(studentInput)
except:
    studentInput2=input("That's not a number, what is 4+5=")
    y=float(studentInput2)
if x==4:
    studentInput2=input("Correct! What is 4+5=")
    y=float(studentInput2)
else:
    studentInput2=input("That's not correct, what is 4+5=")
    y=float(studentInput2)
if y==9:
    print("Correct!")
else:
    print("That's not correct")
print("End")

