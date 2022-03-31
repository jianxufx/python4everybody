#get input from user
score=input('please enter the score between 0.0-1.0 :')

#only a number is allowed
try:
    score=float(score)

except:
    print('bad score')
    exit()

#score [0.0,1.0)

# I donnot know how to campare a float number with 0
# I choose a int instead
if int(score)<0 or int(score)>1:
    print('bad score')
    exit()

#score to grade

if score<0.6:
    print('F')
elif 0.6<=score<0.7:
    print('D')
elif 0.7<=score<0.8:
    print('C')
elif 0.8<=score<0.9:
    print('B')
else:
    print('A')
