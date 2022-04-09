li=[]
dicword=dict()
#open file with mod r
try:
    filehandle =open('words.txt')
except:
    print('file not exsit!\npress any key to exit!')
    res=input()
    exit()

#read each line through  file:

for line in filehandle:

    #we got each line

    #clearn the \n
    line=line.rstrip()

    #split
    templist=line.split()

    for word in templist:
        if word not in li:
            li.append(word)

#built the dict
for key in li:
    #regardless the value of each item
    dicword[key]=1

while True:
    str=input('please enter a string to check if it occurs in the words.txt\n:')
    if str=="done":
        break
    if str not in dicword:
        print(str,'not in the words.txt\n')
    else:
        print(str,'is in the words.txt\n')
