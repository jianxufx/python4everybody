from timeit import default_timer as timer


#open file with r mode

try:
    filehandle=open('c:\\mbox.txt')
except:
    print('file not exist!')
    exit()

#read each line through the file

start=timer()
for line in filehandle:

    #clean the \n
    line=line.rstrip()


    if  not line.startswith('From:'):
        continue

    print(line)
end=timer()

print(end-start)
