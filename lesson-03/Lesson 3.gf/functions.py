#functions: used to wrap code for resuse
def doSomething():
    print('Hello Grace')
    x=7*8*9
    print(x)

uservalidation=input("What's your name?")
if uservalidation==("Grace"):
    doSomething()
else: print('Invalid User')

def verify(a,b,c):
    print('Hello Grace')
    x=a*b*c
    print('The answer is', x)
    return(x)
    # return is the last line of the function. it can be invisible but when u key it in it is the end of the deinfe code

uservalidation=input("What's your name?")
if uservalidation==("Grace"):
    result= verify(7,8,9)
else: print('Invalid User')