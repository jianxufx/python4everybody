li=[]

#open file

try:

    filehandle=open('Romeo.txt')

except:
    print('file not exsit!')
    exit()

#read line by line through the file

for line in filehandle:

    #clearn up the \n at the end of each line
    line=line.strip()

    #split each line into a list of words
    templist=line.split()

    #a loop to check if a word already in the list
    for word in templist:

        #we get each word

        if word not in li:
            li.append(word)

li.sort()
print(li)
