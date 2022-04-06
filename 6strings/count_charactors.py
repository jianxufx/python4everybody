



#count how many times a charactor disappeard int a string

def mycount(str,char):

    times=0

    #if str is empty
    if len(str)<1:
        return 0
    for i in str:
        if i==char:
            times=times+1
    return times


print(mycount('hello','l'))
