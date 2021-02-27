n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff!')

while True:
    line=input('> ')
    if line=='done':
        break
    #continue = skip everything below and go back up
    #break = skip everything and go out of the current loop
    print(line)
print('Done')


