fileHandle = open('programming-together/lesson-05/mbox-short.txt')
#copypath to paste file url
for line in fileHandle: 
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    #to remove the new lines added by the print(line) function, include rstrip
    print(line)

fileHandle = input('Enter file name:')
try:
    fileHandle = open(fileHandle)
    #insurance function to do, if cannot - except
except:
    print('File name cannot be opened:', fileHandle)
    quit()
    #quits python file

