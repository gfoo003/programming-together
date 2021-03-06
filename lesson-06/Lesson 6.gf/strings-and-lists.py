abc = 'with three words'
stuff = abc.split() #use split to convert string to list using white spaces
#Note: muliple spaces counted as one space
print(stuff)
print(len(stuff))
print(stuff[0])


each_line = 'first;second;third'
thing = each_line.split(';') #remember to include aprostophe
print(thing)

def get_lines_from_file(filepath):
    file= open(filepath)
    lines_start_with_from = list()
    for each_line in file:
        if not each_line.startswith("From "): continue #alternative: if each_line.startswith("From "):
        lines_start_with_from.append(each_line) # alternative: indent lines_starts_with_from.append (each_line)
    return lines_start_with_from

days_of_the_week = list()
lines = get_lines_from_file("lesson-05/mbox-short.txt")
for each_line in lines:
    words = each_line.split()
    days_of_the_week.append(words[2])
print(days_of_the_week)




