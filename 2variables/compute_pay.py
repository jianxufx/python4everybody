hours=input('please enter your hours:')
rate=input('please enter your rate:')

#note:the return value of input is a string type
pay=int(hours)*float(rate)

print('your Pay is :',round(pay,2))
