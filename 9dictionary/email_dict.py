'''
Exercise 3: Write a program to read through a mail log,
build a histogram using a dictionary to count how many messages have come from each email address,
and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}


'''


#oen file with r mode

email_dict={}

try:

    filehandle=open('mbox-short.txt')

except:
    print('file not exsit!')
    a=input('Press any key to continue:')
    exit()

#read each line through file:

for line in filehandle:

    #we got each line here

    #we only care the line starts with 'From '

    if not line.startswith('From'):
        continue

    #clearn the \n
    line=line.strip()

    #split the line  into a list of words
    #line[1] is what we want
    line=line.split()

    #build the dictionary
    email_dict[line[1]]=email_dict.get(line[1],0)+1


print(email_dict)
