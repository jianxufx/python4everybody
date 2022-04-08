#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008



#open file with r mode

try:
    filehandle =open('c:\\mbox.txt')

except:
    print('file not exist!')
    exit()


#read each line through file

for line in filehandle:
    #now we got each line

    #we only match the line starts with From

    if line.startswith('From '):
        li=line.split()
        print(li[2])
