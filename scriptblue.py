from random import randint

def locconvert(u,v):
    if u < 10: 
        loc = '0'+str(int(u))
    else:
        loc = str(int(u))
    if v < 10:
        loc = loc + '0'+str(int(v))
    else:
        loc = loc + str(int(v))
    return loc

def Goto(x,y,xe,ye):
    S = 0
    if x<xe: 
        S = 2
    elif x>xe: 
        S = 4
    else : 
        if y<ye: S = 3
        elif y>ye: S = 1
    return S
    
def Stay(x,y,xp,yp,xq,yq):
    xa = min(xp,xq)
    xb = max(xp,xq)
    ya = min(yp,yq)
    yb = max(yp,yq)
    S = 0
    if x>xa and x<xb and y>ya and y<yb:
        S = randint(1,4)
    else :
        if x<=xa:
            S = 2
        elif x>=xb:
            S = 4
        else:
            if y<=ya:
                S = 3
            elif y>=yb:
                S = 1
    return S
        
def ActRobot(robot):
        T = 0
        inisig =  robot.GetInitialSignal()
        sig = robot.GetCurrentBaseSignal()
        x,y = robot.GetPosition()

        ##getting location of base
        if inisig[2] == 0: xb = int(inisig[3])
        else : xb = int(inisig[2]+inisig[3])

        if inisig[4] == 0: yb = int(inisig[5])
        else : yb = int(inisig[4]+inisig[5])

        totalvirus = robot.GetVirus()

        ##movement mechanism
        if robot.investigate_up()=='enemy-base' or robot.investigate_down()=='enemy-base' or robot.investigate_left()=='enemy-base' or robot.investigate_right()=='enemy-base' or robot.investigate_nw()=='enemy-base' or robot.investigate_ne()=='enemy-base' or robot.investigate_sw()=='enemy-base' or robot.investigate_se()=='enemy-base' :
            robot.DeployVirus(totalvirus)
        else:
            if inisig[0]=='d' :
                if robot.GetTotalElixir() > 2500: 
                    if inisig[1]=='A':
                        T = Goto(x,y,xb+1,yb-1)
                    elif inisig[1]=='B':
                        T= Goto(x,y,xb+1,yb+1)
                    elif inisig[1]=='C':
                        T= Goto(x,y,xb-1,yb+1)
                    elif inisig[1]=='D':
                        T= Goto(x,y,xb-1,yb-1)
                    elif inisig[1]=='E':
                        T = Goto(x,y,xb-2,yb)
                    elif inisig[1]=='F':
                        T = Goto(x,y,xb-1,yb)
                    elif inisig[1] == 'G':
                        T = Goto(x,y,xb,yb-2)
                    elif inisig[1] == 'H':
                        T = Goto(x,y,xb,yb+2)
                else: 
                    if x == xb:
                        if xb >= 20: T = 2
                        elif xb<20 : T = 4
                    elif y == yb:
                        if yb >= 20 :T = 3
                        elif yb<20 : T = 1
                    else : T = randint(1,4) 

            elif inisig[0]=='c' : 
                if robot.GetTotalElixir() < 2500 :
                    if inisig[1]=='1':
                        T = Goto(x,y,xb+1,yb-1)
                    elif inisig[1]=='2':
                        T= Goto(x,y,xb+1,yb+1)
                    elif inisig[1]=='3':
                        T= Goto(x,y,xb-1,yb+1)
                    elif inisig[1]=='4':
                        T= Goto(x,y,xb-1,yb-1)
                    
                else:   
                    if xb>=20 and x <= xb: T = 2
                    elif xb<20 and x>=xb : T = 4
                    elif yb>20 and y <= yb: T= 3
                    elif yb<20 and y >= yb: T = 1
                    else : T = randint(1,4)
            elif inisig[0]=='a' :
                if len(sig)<=4: 
                    T = randint(1,4)
                else:
                    T = Goto(x,y,int(sig[4]+sig[5]),int(sig[6]+sig[7]))
            elif inisig[0] == 'm' :
                T = Stay(x,y,10,10,30,30)

            
            #Detecting opponents
            
            if inisig[0] == 'd' :
                if robot.investigate_up()=='enemy' or robot.investigate_down()=='enemy' or robot.investigate_left()=='enemy' or robot.investigate_right()=='enemy' or robot.investigate_nw()=='enemy' or robot.investigate_ne()=='enemy' or robot.investigate_sw()=='enemy' or robot.investigate_se()=='enemy' :
                    robot.DeployVirus(totalvirus)
            elif inisig[0] == 'c' and int(inisig[1])<5:
                    if robot.investigate_up()=='enemy' or robot.investigate_down()=='enemy' or robot.investigate_left()=='enemy' or robot.investigate_right()=='enemy' or robot.investigate_nw()=='enemy' or robot.investigate_ne()=='enemy' or robot.investigate_sw()=='enemy' or robot.investigate_se()=='enemy' :
                        robot.DeployVirus(totalvirus)
            elif inisig[0] == 'c':
                if robot.investigate_up()=='enemy' or robot.investigate_down()=='enemy' or robot.investigate_left()=='enemy' or robot.investigate_right()=='enemy' or robot.investigate_nw()=='enemy' or robot.investigate_ne()=='enemy' or robot.investigate_sw()=='enemy' or robot.investigate_se()=='enemy' :
                    robot.DeployVirus(500)
            elif inisig[0] == 'a' or inisig[0]=='m':
                if robot.investigate_up()=='enemy' or robot.investigate_down()=='enemy' or robot.investigate_left()=='enemy' or robot.investigate_right()=='enemy' or robot.investigate_nw()=='enemy' or robot.investigate_ne()=='enemy' or robot.investigate_sw()=='enemy' or robot.investigate_se()=='enemy' :
                    if totalvirus>8000:
                        robot.DeployVirus(totalvirus/4)
                    elif totalvirus>2000:
                        robot.DeployVirus(1000)    
                    elif totalvirus>800:
                        robot.DeployVirus(500)
                    
                
        return T


def ActBase(base):
    x = 0
    L = base.GetListOfSignals()


    u,v = base.GetPosition()
    loc = locconvert(u,v)

    if len(base.GetYourSignal())==0:
        TEl = base.GetElixir()
    else :
        TEl = int(base.GetYourSignal()[0:4])
    base.SetYourSignal(str(TEl))

    #getting location in string format  1,12 loc = '0112
    

    #maaking robots
    el = base.GetElixir()
    if el > TEl-400:
        x = (TEl-el)//50 + 1
        base.create_robot('d'+str(chr(x+64))+loc)
    elif el > TEl - 600:  
        x = (TEl - 400 -el)//50 + 1
        base.create_robot('c'+str(x)+loc)
    elif el > TEl - 1300:
        x = (TEl - 600 - el)//50 + 1
        base.create_robot('m'+str(x)+loc)
    elif el > TEl/20 :  
        x = (TEl - 1300 -el)//50 + 1
        base.create_robot('a'+str(x)+loc)


   
    return
