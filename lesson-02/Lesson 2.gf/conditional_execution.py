#<, <=, ==, >=, >, != less than, less than or equal to, equal to, more than or equal to, more than, not equal

a=5
if (a>0):
    print("hello")

#two way decisions can use "if" "else"
#there must be an indentation and semicolon after each if

x=1
y=10
if x==0:
    if y==10:
        print("x and y are true")
    print("only x is true")
print("only y is true")
print("End")

#multi-way
#order matters, if it does not see a false, it does not continue
x=21
if x<2:
    print('small')
elif x<10:
    print('medium')
elif x<20:
    print('large')
else:
    print('Something else')
print('All Done')

#try/except adds some insurance
