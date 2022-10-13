# 9 �������
#from pickle import TRUE


goal = False

for n in range(1, 100):
    if(goal == True):
      break
    for a in range(1, 110):
        if(goal == True):
            break

        for b in range(2, 110):
            if(goal == True):
                break

            for c in range(3, 101):
                if(goal == True):
                    break

                if (n**3 == (a**3 + b**3 + c**3)):
                    print('N-->',n)
                    print('N1-->',a)
                    print('N2-->',b)
                    print('N3-->',c)
                    goal = True
                    break

goal = False
a = 1
b = 2
c = 3
n = 0

while(goal == False):
    if (n**3 == (a**3 + b**3 + c**3)):
        print('N-->',n)
        print('N1-->',a)
        print('N2-->',b)
        print('N3-->',c)
        goal = True

    if(a>10):
        a = 1
        b = 2
        c = 3
        n+=1

    a+=1
    b+=1
    c+=1

#print('end')
