#
def myfloor(x):
    # if x a type of x.0
    # o is a type of x.0
    if(float(x)==int(x)):
        return x
    # if x is not a type of x.0
    if x>0:
        return int(x)
    else :
        return int(x)-1

def myceil(x):
    # if x a type a x.0
    # o is a type of x.0
    if(float(x)==int(x)):
            return x
    # if x is not a type of x.0
    if x>0:
        return int(x)+1
    else :
        return int(x)


print(myceil(0))
print(myceil(1))
print(myceil(-1))
print(myceil(5.6))
print(myceil(-7.8))
print('-'*50)
print(myfloor(0))
print(myfloor(5))
print(myfloor(-500))
print(myfloor(-100.5))
print(myfloor(456.78))
