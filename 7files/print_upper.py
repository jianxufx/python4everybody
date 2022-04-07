import os
#prompt
file=input('please enter a file name:')

try:
    filehandle=open(file)

except:
    print('file not exist!')
    exit()


#read each line through the file

for line in filehandle:
    print(line.upper())
