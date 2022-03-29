#read file

filehandle=open('c:\\mbox.txt','r')

words=list()
dc=dict()

#read line through the file

for line in filehandle:

    #now we get each line

    #we want the line starts with "From" or "from"
    if not (line.startswith('From') or line.startswith('from')):
        continue

    #clean up the line
    line=line.strip('')

    #split words from a line

    words=line.split(' ')

    #now we  got a list full of  separated words

    #and list[2] is the item we need

    #exculue the case like this   "From: zqian@umich.edu"
    if len(words)<3:
        continue
    else:
        dc[words[2]]=dc.get(words[2],0)+1

print(dc)
