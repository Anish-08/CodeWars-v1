from random import randint


def ActRobot(robot):
        T = 0
        inisig =  robot.GetInitialSignal()
        sig = robot.GetCurrentBaseSignal()
        x,y = robot.GetPosition()

        '''getting location of base'''
        if inisig[2] == 0: xb = int(inisig[3])
        else : xb = int(inisig[2]+inisig[3])

        if inisig[4] == 0: yb = int(inisig[5])
        else : yb = int(inisig[4]+inisig[5])

        totalvirus = robot.GetVirus()

        '''movement mechanism'''
        if robot.investigate_up()=='enemy-base' or robot.investigate_down()=='enemy-base' or robot.investigate_left()=='enemy-base' or robot.investigate_right()=='enemy-base' or robot.investigate_nw()=='enemy-base' or robot.investigate_ne()=='enemy-base' or robot.investigate_sw()=='enemy-base' or robot.investigate_se()=='enemy-base' :
            robot.DeployVirus(totalvirus)
        else:
            if inisig[0]=='d' :
                if robot.GetTotalElixir() > 3000: 
                    if inisig[1]=='1':
                        if x<xb+1:
                            T = 2
                        elif x>xb+1:
                            T = 4
                        else :
                            if y > yb-1:
                                T = 1
                            elif y < yb-1:
                                T = 3
                    elif inisig[1]=='2':
                        if x<xb-1:
                            T = 2
                        elif x>xb-1:
                            T = 4
                        else :
                            if y > yb-1:
                                T = 1
                            elif y < yb-1:
                                T = 3
                    elif inisig[1]=='3':
                        if x<xb+1:
                            T = 2
                        elif x>xb+1:
                            T = 4
                        else :
                            if y > yb+1:
                                T = 1
                            elif y < yb+1:
                                T = 3
                    elif inisig[1]=='4':
                        if x<xb-1:
                            T = 2
                        elif x>xb-1:
                            T = 4
                        else :
                            if y > yb+1:
                                T = 1
                            elif y < yb+1:
                                T = 3
                else: 
                    if x == xb:
                        if xb >= 20: T = 2
                        elif xb<20 : T = 4
                    elif y == yb:
                        if yb >= 20 :T = 3
                        elif yb<20 : T = 1
                    else : T = randint(1,4) 

            elif inisig[0]=='c' :
                if robot.GetElixir() > 500 and len(sig)>0:
                    xe = int(sig[0]+sig[1])
                    ye = int(sig[2]+sig[3])
                    if x<xe: T = 2
                    elif x>xe: T = 4
                    else : 
                        if y<ye: T = 3
                        elif y>ye: T = 1
                else: 
                    if x == xb:
                        if xb >= 20: T = 2
                        elif xb<20 : T = 4
                    elif y == yb:
                        if yb >= 20 :T = 3
                        elif yb<20 : T = 1
                    else : T = randint(1,4)
            elif inisig[0]=='a': 
                T = randint(1,4)

            
            '''Detecting opponents'''
            
            if inisig[0] == 'd' :
                if robot.investigate_up()=='enemy' or robot.investigate_down()=='enemy' or robot.investigate_left()=='enemy' or robot.investigate_right()=='enemy' or robot.investigate_nw()=='enemy' or robot.investigate_ne()=='enemy' or robot.investigate_sw()=='enemy' or robot.investigate_se()=='enemy' :
                    robot.DeployVirus(min(2000,totalvirus))
            elif inisig[0] == 'c':
                    if robot.investigate_up()=='enemy' or robot.investigate_down()=='enemy' or robot.investigate_left()=='enemy' or robot.investigate_right()=='enemy' or robot.investigate_nw()=='enemy' or robot.investigate_ne()=='enemy' or robot.investigate_sw()=='enemy' or robot.investigate_se()=='enemy' :
                        robot.DeployVirus(500)
            elif inisig[0] == 'a':
                if robot.investigate_up()=='enemy' or robot.investigate_down()=='enemy' or robot.investigate_left()=='enemy' or robot.investigate_right()=='enemy' or robot.investigate_nw()=='enemy' or robot.investigate_ne()=='enemy' or robot.investigate_sw()=='enemy' or robot.investigate_se()=='enemy' :
                    if totalvirus>8000:
                        robot.DeployVirus(2000)
                    elif totalvirus>2000:
                        robot.DeployVirus(1000)    
                    elif totalvirus>800:
                        robot.DeployVirus(500)
                    
                
        return T


def ActBase(base):
    x = 0
    L = base.GetListOfSignals()
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
    elif el > 1600:  
        x = (1800-el)//50 + 1
        base.create_robot('c'+str(x)+loc)
    elif el > 800:  
        x = (1600-el)//50 + 1
        base.create_robot('a'+str(x)+loc)


   
    return
