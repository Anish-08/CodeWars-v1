from random import randint


def ActRobot(robot):
        T = randint(1,4)

        if robot.GetVirus() > 1000:
                robot.DeployVirus(200)  
        '''
        initsig = robot.GetInitialSignal()
        sig = robot.GetCurrentBaseSignal()
        if len(sig) != 0:
                xe = int (sig[0]+sig[1])
                ye = int (sig[2]+sig[3])
                if initsig[0] == 'c':
                        T = randint(1,4)
                elif initsig[0] == 'a':
                        xr,yr =  robot.GetPosition()
                        if xr < xe:
                                T = 2
                        elif xr > xe:
                                T = 4
                        elif xr == xe:
                                if yr < ye:
                                        T = 3
                                elif yr > ye:
                                        T = 1


        
        '''
        return T
        


def ActBase(base):
    '''
    Add yr code here
    
    
    el = base.GetElixir()
    if el > 1800:
            x = (2000-el)/50 + 1
            base.create_robot('d'+str(x))      
             Defenders 
    elif el>1000:
            x=(1800-el)/50 + 1
            base.create_robot('a'+str(x))        
            attackers
    
    elif el > 800:
            x = (1000-el)/50 + 1
            base.create_robot('c'+str(x))       
            collectors          
    x,y = base.GetPosition()  
    base.SetYourSignal(str(x//10)+str(x%10)+str(y//10)+str(y%10))  
    '''    

    if base.GetElixir() > 500:
            base.create_robot('')
    return