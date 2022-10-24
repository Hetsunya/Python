# 9 �������
#from pickle import TRUE

def laba():
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
                        print('N-->', n)
                        goal = True
                        break
    '''
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
            a = 2
            b = 3
            c = 4
            n+=1
    
        a+=1
        b+=1
        c+=1
    
    print('end')
    '''
    import random as rnd

    g = []
    digits = []
    for i in range (1, 1000):
        a = rnd.randint(1, 10)
        b = rnd.randint(1, 10)
        c = rnd.randint(1, 10)
        if a == b or b == c or a == c:
            continue
        for n in range(1, 10):
            #ВОЗМОЖНО ЗАМЕДЛЯЕТ
            #for z in range(0, len(g)):
                #if (a ** 3 + b ** 3 + c ** 3) == g[z]:
                    #continue
            #for z in range(0, len(g)):
               #if (a ** 3 + b ** 3 + c ** 3) == g[z]:
                    #break
            if (n ** 3 == (a ** 3 + b ** 3 + c ** 3)):
                digits.append(n)
            else:
                g.append(a ** 3 + b ** 3 + c ** 3)

    print('N-->', min(digits))

import time
start_time = time.time()
laba()
print("--- %s seconds ---" % (time.time() - start_time))