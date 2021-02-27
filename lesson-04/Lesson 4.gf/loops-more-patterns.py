# foundAThree=False
# print('Before', foundAThree)
# for number in [9,41,12,3,74,15]:
#     if(number == 3):
#         foundAThree=True
#         print(foundAThree, number)
#         #to include this value again so that if true, the value will print
#         break
#         #to include this break to stop once the value is found
#     print(foundAThree,number)
# print('After', foundAThree)

smallest=None
print('Before', smallest)
for number in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        #use 'is' sparingly, only on booleans or ifs or true false statements
        #'is' is a stronger form of equal, has to be exact
        smallest=number
    elif number<smallest:
        smallest=number
    print(smallest, number)
print('After', smallest)
