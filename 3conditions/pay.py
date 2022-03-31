hours=input('please enter the hours:')
rate=input('please enter the rate:')



try:
    #if we got a str from the input
    #we would catch a exception
    hours=float(hours)
    rate=float(rate)

except:
    print('number only!')
    exit()

if hours<=40:
    pay=hours*rate
    print('your payment is :',round(pay,1))
else:

    #pay=base+overtime*rate*1.5
    pay=40*rate+(hours-40)*rate*1.5
    print('your payment is :',round(pay,1))
