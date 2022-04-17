'''
Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
 Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195

'''
email_count=dict()
#read file with r mode
try:
    filehandle=open('mbox.txt')
except:
    print('file not exsit!')
    a=input('Press any key to continue:')
    exit()


#read each line through the file

for line in filehandle:

    #we got the each line

    #we only care the lines starts with 'From '

    if not line.startswith('From '):
        continue

    #split

    line=line.split()

    #line[1] is what we want

    #build the dictionary
    email_count[line[1]]=email_count.get(line[1],0)+1


li=[]

for key,value in email_count.items():
    li.append((value,key))

li.sort(reverse=True)

email=li[0][1]
count=li[0][0]

print(email,count)
