try:
    filehandle=open('c:\\mbox-short.txt')

except:
    print('file not exist!')
    exit()


for line in filehandle:
    line=line.rstrip()
    if line.find('@uct.ac.za')!=-1:
        print(line)
