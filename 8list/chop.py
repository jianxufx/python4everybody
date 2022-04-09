def chop(li):

    li.pop(0)
    li.pop(-1)


def middle(li2):
    temp=li2[:]

    temp.pop(0)
    temp.pop(-1)

    return temp





li=[1,2,3,4]
chop(li)
print(li)

li2=[6,7,8,9]
print(middle(li2))
