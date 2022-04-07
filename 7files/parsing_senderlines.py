
#open file with r mode

try:
    filehandle=open('c:\\mbox.txt')
except:
    print('file not exist!')
    exit()

#read each line through the file
for line in filehandle:

    #clean the \n
    line=line.rstrip()


    if  line.startswith('From:'):
        print(line)
