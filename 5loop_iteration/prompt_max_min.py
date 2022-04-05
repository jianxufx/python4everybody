max=None
min=None
while True:
    num=input('please enter a number:')

    if num=='done':
        break
    try:
        num=float(num)
    except:
        print('only numbers are allowed')
        continue

    #the first input of user
    if max==None:
        max=num
    else:
        if num>=max:
            max=num

    if min==None:
        min=num
    else:
        if num<=min:
            min=num

print(max,min)
