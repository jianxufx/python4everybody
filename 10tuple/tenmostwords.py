#we need the result like this  to:10 of :5 etc
#the best way is to build a dictionary

#read file wirth r mode

try:
    filehandle=open('romeo-full.txt')
except:
    print('file not exsit!')
    a=input('Press any key to continue:')
    exit()

word_count={}
li=list()
word_special='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

#read each line trough the file

for line in filehandle:

    #we got each line here

    #clean up the \n
    line=line.strip()

    #delete the special charator
    map_delte =line.maketrans('','',word_special)
    line=line.translate(map_delte)

    #lower

    line=line.lower()

    #split a line into a list of words
    words=line.split()

    #build the dictionary
    for word in words:
        word_count[word]=word_count.get(word,0)+1


#list have the sort method
for i ,k in word_count.items():
    #li.append((k,i)) also works
    li.append([k,i])

li.sort(reverse=True)

#print the 10 most occurances of the words
for i,k in li[:10]:
    print(k,i)
