'''
Exercise 2: This program counts the distribution of the hour of the day for each of the messages.
You can pull the hour from the “From” line by finding the time string
and then splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out the counts, one per line,
sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

sample line :From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008


'''
timecount=dict()
#read file with r mode
try:
    filehandle =open('mbox-short.txt')
except:
    print('file not exist!')
    a=input('Please any key to continue:')
    exit()

#read each line through the file

for line in filehandle :

    #we get each line here

    #we care the line starts with "From "

    if not line.startswith('From '):
        continue

    #clearn the \n

    line=line.strip()

    #split

    wordslist=line.split()

    #wordslist[-2] is what we want

    #split the wordslist[-2] with :

    timelist=wordslist[-2].split(':')

    #build the dictionary
    #timelist[0] is what we want

    timecount[timelist[0]]=timecount.get(timelist[0],0)+1

li=[]

for i ,k in timecount.items():
    li.append((i,k))

li.sort()

for i ,k in li:
    print(i,k)
