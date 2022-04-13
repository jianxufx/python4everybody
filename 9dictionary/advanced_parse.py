del_char='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#empty dict
words={}

#open file with r mode
try:
    filehandle =open('words.txt')
except:
    print('file not exist')
    a=input('Press any key to continue:')
    exit()

#read each line through file:

for line in filehandle:

    #we get each line

    #clean the \n at the end of line
    line=line.rstrip()

    #delete the special charachter
    line=line.translate(line.maketrans('','',del_char))

    #split the line to be  a list of words  by space
    tempwords=line.split()

    #build the dict

    for word in tempwords:
        word=word.lower()
        words[word]=words.get(word,0)+1


#how to arphabet the keys int the dict?
#because dict donnot have the sort method
#but list have the sort method
#we need to build a sorted list

'''
#build the alphabet list
keys=[]

for key in words.keys():
    keys.append(key)

keys.sort()

#print the alphabet dict

for name in keys:
    print(name,words[name])


print('*'*20)
'''

#*****************************************************************

#how to print the most used word by decrentment
#we are going to do this like the alphabet list

#from A:B  to B:A

# can anyone help me ?
#*****************************************************************


# another method to build the alphabet result
#we use tuple to the pair
li=[]
for i,k in words.items():
    li.append((i,k))

li.sort()

for m,n in li:
    print(m,n)


print('-'*30)



#print the dict ranked by value

livalue=[]

for i,k in words.items():
    livalue.append((k,i))

livalue.sort(reverse=True)

for m,n in livalue:
    print(n,m)
