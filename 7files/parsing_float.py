#X-DSPAM-Confidence: 0.8475
#prompt

file =input('please enter a file name:')

#try to open it

try:

    filehandle=open(file)

except:
    print('file not exist')
    exit()


count=0
floatnum=0

#read each line through the file
for line in filehandle:

    #only capture the line startswith X-DSPAM-Confidence
    if line.startswith('X-DSPAM-Confidence:'):

        #count
        count=count+1

        #clean the \n
        line=line.rstrip()

        #parseing the float number
        index=line.find(':')

        #copy the float number
        num=line[index+1:]

        #add it
        floatnum=floatnum+float(num)

print('count:',count,'average Confidence:',floatnum/count)
