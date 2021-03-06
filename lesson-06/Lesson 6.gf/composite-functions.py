# composite functions: pass two functions onto the same argument

def indexesOf(list):
    return(range(len(list)))

friends = ['joseph', 'glenn', 'sally']
print(indexesOf(friends))
print(range(3))

for n in indexesOf(friends):
    print(n) #0,1,2

for number in range(10,20):
    print(number)

#overload: same function name but different signatures
range(a, b) #[a, a+1, ..., b-1] where a <= b-1 === a+1 <= b
range (b) #range(0,b)
