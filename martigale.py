import random
import sys

START_MONEY=2**10
BET_START=1
OBJECTIVE_MONEY=START_MONEY*2
NUMBER_OF_MARTIGALE=1000

GLOBAL_WIN=0
GLOBAL_LOST=0

for i in range(NUMBER_OF_MARTIGALE):
    print("START_MONEY=", START_MONEY, "current_bet=",BET_START)
    current_money=START_MONEY
    while current_money>=1 and current_money<OBJECTIVE_MONEY:
        objective_money=current_money+1
        current_bet=BET_START
        while current_money>=current_bet and current_money!=objective_money:
            if(random.randrange(2)==1):
                current_money+=current_bet
                #print("WON, current_bet=", current_bet,"current_money=", current_money)
            else:
                current_money-=current_bet
                current_bet=current_bet*2
                #print("LOST, doubling bet to=", current_bet ,"current_money=", current_money)
        if(current_money!=objective_money):
            #print("BIG LOST, restarting to ", BET_START ,"current_money=", current_money)
            pass
        else:
            #print("BIG WIN, restarting to ", BET_START ,"current_money=", current_money)
            pass
                
                
    if(current_money==0):
        print("WE LOST GLOBALLY :'(", i)
        GLOBAL_LOST+=1
    elif(current_money>=OBJECTIVE_MONEY):
        print("WE WON GLOBALLY YOUPI ", current_money, i)
        GLOBAL_WIN+=1
    else:
        print("MY CODE IS BUGGY")
        sys.exit()
        
        
print("GLOBAL_WIN=", GLOBAL_WIN, "GLOBAL_LOST=", GLOBAL_LOST, "GLOBAL_LOST", 100.0*GLOBAL_WIN/(GLOBAL_WIN+GLOBAL_LOST))