firstName = input("What is your firstName?")
lastName = input("What is your surname?")
gender = input("Male/Female?")
ifFemale = None
#variable needs to exist for line 10 to work
if gender == 'Female':
    ifFemale = True
else:
    ifFemale = False
gender = 'Female' if ifFemale else 'Male'
result = f'I am {firstName} {lastName} and I am a {gender}.'
print (result)