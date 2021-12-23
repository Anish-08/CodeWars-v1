from random import randint


def ActRobot(robot):
        T = 0
        inisig =  robot.GetInitialSignal()
        sig = robot.GetCurrentBaseSignal()

        if inisig[2] == 0: xb = int(inisig[3])
        else : xb = int(inisig[2]+inisig[3])

        if inisig[4] == 0: yb = int(inisig[5])
        else : yb = int(inisig[4]+inisig[5])

        if inisig[0]=='d' :
            if inisig[1]=='1':
                if robot.GetPosition() == (xb,yb):
                    T = 1
                elif robot.GetPosition() == (xb,yb-1):
                    T = 2
            elif inisig[1]=='2':
                if robot.GetPosition() == (xb,yb):
                    T = 2
                elif robot.GetPosition() == (xb+1,yb):
                    T = 3
            elif inisig[1]=='3':
                if robot.GetPosition() == (xb,yb):
                    T = 3
                elif robot.GetPosition() == (xb,yb+1):
                    T = 4
            elif inisig[1]=='4':
                if robot.GetPosition() == (xb,yb):
                    T = 4
                elif robot.GetPosition() == (xb-1,yb):
                    T = 1


        elif inisig[0]=='a' :
            if robot.GetTotalElixir() > 4000 and len(sig)>0:
                xe = int(sig[0]+sig[1])
                ye = int(sig[2]+sig[3])
                x,y = robot.GetPosition()
                if x<xe: T = 2
                elif x>xe: T = 4
                else : 
                    if y<ye: T = 3
                    elif y>ye: T = 1
            else: T = randint(1,4)
        elif inisig[0]=='c': 
            T = randint(1,4)


        return T


def ActBase(base):
    x = 0
    '''getting location in string format'''
    u,v = base.GetPosition()
    if u < 10: 
        loc = '0'+str(int(u))
    else:
        loc = str(int(u))
    if v < 10:
        loc = loc + '0'+str(int(v))
    else:
        loc = loc + str(int(v))

    '''maaking robots'''
    el = base.GetElixir()
    if el > 1800:
        x = (2000-el)//50 + 1
        base.create_robot('d'+str(x)+loc)
    elif el > 1200:  
        x = (1800-el)//50 + 1
        base.create_robot('a'+str(x)+loc)
    elif el > 800:  
        x = (1200-el)//50 + 1
        base.create_robot('c'+str(x)+loc)
    return
