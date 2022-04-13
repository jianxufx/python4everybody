'''
Exercise 5: This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from (i.e., the whole email address).
At the end of the program, print out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}


'''

#sapmle here:  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008


#open the file with r mode

try:
    filehandle =open('mbox.txt')
except:
    print('file not exsit!')
    a=input('Press any key to continue:')
    exit()

domain_dict={}

#read each line through the file:

for line in filehandle:

    #we get each line here

    #we care about the line starts with 'From '

    if not line.startswith('From '):
        continue

    #clear the \n
    line=line.strip()

    #split the word into a list of words
    wordslist=line.split()

    #we care the wordlist[1]
    address=wordslist[1].split('@')

    #we care address[1]

    #build dictionary by a pair of  domain: count
    domain_dict[address[1]]=domain_dict.get(address[1],0)+1


#after the loop,the dictionary will be built

print(domain_dict)
