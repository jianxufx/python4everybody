#read file

#exception
try:
    filehandle=open('c:\\mbox.txt','r')

except:
    print("file missing or permision denied!")
    exit()

words=list()
emailcount=dict()

#read lines through the file

for line in filehandle:

    #now we get each line
    #clearn up the line
    line=line.strip()

    #we only accept the string starts with 'From'
    if not line.startswith('From'):
        continue

    #split
    words=line.split(' ')

    #now we get a list of words separated from each line

    #words[1] is what we want

    emailcount[words[1]]=emailcount.get(words[1],0)+1


print(emailcount)
