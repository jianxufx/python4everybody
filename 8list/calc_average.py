li=[]
count=0

#get number from user

while True:
    num=input('please enter a number:')
    if num=='done':
        break

    try:
        num=float(num)

    except:
        print('number only')
        continue

    count=count+1
    li.append(num)

print('average is :',sum(li)/count)
