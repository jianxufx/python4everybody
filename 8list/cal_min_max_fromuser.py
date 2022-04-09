li=[]

while True:
    num=input('please enter a number:')

    if num=='done':
        break

    try:
        num=float(num)
    except:
        print('only numbers!')
        continue


    li.append(num)

print('max number is :',max(li),'min number is :',min(li))
