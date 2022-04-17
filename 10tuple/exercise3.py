'''
Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
Your program should convert all the input to lower case and only count the letters a-z.
Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
Find text samples from several different languages and see how letter frequency varies between languages.
Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''




#we need to build the dictionary that contains the mapping like this
# word:count



word_special='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#read file with r mode

try:
    filehandle =open('我是一个学生.txt',encoding='utf-8')
except:
    print('file not exist!')
    a=input('Press any key to continue:')
    exit()

word_count=dict()

#read each line through

for line in filehandle:

    #we get each line here

    #clearn the \n
    line =line.strip()

    #clearn the special words

    map=line.maketrans('','',word_special)
    line=line.translate(map)

    #all lower
    line=line.lower()

    #spit
    wordslist=line.split()

    #build the dictionary
    for word in wordslist:
        word_count[word]=word_count.get(word,0)+1


li=list()

for i,k in word_count.items():
    li.append((k,i))

li.sort(reverse=True)

#top 20 most frequency words
for i,k in li[:20]:
    print(k,i)
