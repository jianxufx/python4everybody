txt = 'but soft what light in yonder window breaks'

a=list()

for word in txt.split():
    a.append([len(word),word])

a.sort(reverse=True)

'''
a=list('hello hanmeimei jim lilei')

for i,k in a.


'''
