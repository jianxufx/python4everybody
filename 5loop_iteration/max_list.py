#print the max number of a given list

li=[-50,0,10,13.5,100.89,27149]


def max_list(li):

    #no empty list
    if(len(li)<1):
        print('empty list is not allowed')
        return None

    #only numbers allowed
    for item in li:
        if  not(type(item)==int or type(item)==float):
            print('only numbers allowed')
            return None

    #we  think the first item in the list as the max number.
    max=li[0]

    for num in li:
        if num>=max:
            max=num
    #end of the loop
    return max

print(max_list(li))
