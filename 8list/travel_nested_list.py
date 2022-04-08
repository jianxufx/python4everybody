
#li is a  source list
#res is a list for result
def travel(li,res):

    if len(li)==0:
        print('None')
        return None

    #get each item through the list
    for item in li:

        # this item is a int or float or string
        if type(item)!=list:
            res.append(item)
            print(item)

        #this item is a list
        else:
            return travel(item,res)



a=[1,2,3,[27149,'tesv',[3.1415,80]]]
b=[]
res=[]

travel(a,res)
print('-'*20)
print(res)
