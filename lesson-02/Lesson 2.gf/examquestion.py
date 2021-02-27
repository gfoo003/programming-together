studentInput = input('What is 5*5?')
#scope
intConvertedstudentInput = 0
try:
    #to test if this is a integer
    intConvertedstudentInput = float(studentInput)
except:
    #exception handling code
    print("This is not a number")
if(intConvertedstudentInput== 5*5):
    print("Correct!")
else:
    print("Wrong")
