total=0
count=0
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp) #change to interger
    total = total +value
    count = count+1
average = total/count
print ('Average:', average)

#interesting to note this takes up higher memory because
#in each loop it adds to the numlist, remembers it and holds it to the list
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)

# append: add item to the end of the list
