x=7
while (x < 10):
    print(f"x is {x}")
    print("x divde by 4 remainder 1")
    if (x % 2 ==0): #check if even number
        print('x is even')
        break
    else:
        print('x is odd')
        x=x-1
        continue


# x=0
# while (x<10):
#     x+= 1
#     print(x)
#     if (x % 2 == 0):
#         print (f"{x} is even")
#     elif (x % 2 == 1):
#         print (f"{x} is odd")
# print ('Done')


