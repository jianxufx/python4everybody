#
def myfloor(x):
    # if x a type a x.0
    if(float(x)==int(x)):
        return x
    # if x is not a type of x.0
    if x>0:
        return int(x)
    elif x<0:
        return int(x)-1
    else:
        return 0
def myceil(x):
    # if x a type a x.0
    if(float(x)==int(x)):
            return x
    # if x is not a type of x.0
    if x>0:
        return int(x)+1
    elif x<0:
        return int(x)
    else:
        return 0

print(myceil(0))
print(myceil(1))
print(myceil(-1))
print(myceil(5.6))
print(myceil(-7.8))
