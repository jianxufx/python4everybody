'''
Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week.
At the end of the program print out the contents of your dictionary (order does not matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}


'''

#open the file with r mode
try:

    filehandle=open('mbox.txt')
except:
    print('file not exist!')
    a=input('Press any button to contine:')
    exit()

li=[]
dict_day={}
#read each line thrught the file:
for line in filehandle:
    #we got each line here

    #we only care ahout the line starts with 'From '

    if not line.startswith('From '):
        continue

    #clean the \n
    line.strip()

    #split each line into a list of words
    li=line.split()

    #build the dict

    #li[2] is the date variable
    dict_day[li[2]]=dict_day.get(li[2],0)+1


print(dict_day)
