#open a file with r mode
try:

    filehandle=open('mbox.txt')

except:
    print('file not exist!')
    exit()

#read each line by line throgu the file

for line in filehandle:

    #we got the line startswith "From:"
    if line.startswith('From:'):

        #clearn up the \n
        line=line.rstrip()

        #split
        templist=line.split()
        print(templist[1])
