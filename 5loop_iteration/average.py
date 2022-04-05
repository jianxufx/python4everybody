
count=0
sum=0
while True:
    num=input('please enter a number:')

    if num=='done':
        break
    try:
        num=float(num)
    except:
        print('only numbers are allowed')
        continue

    count=count+1
    sum=sum+num

average=sum/count
print(sum,count,average)
