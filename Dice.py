import random
import time

dicenum = random.randint(1,6)

print("you dice number is :" , dicenum)

if dicenum == 6 :
    dicenum = random.randint(1,6)
    print ("you have a new chance")
    time.sleep(3)
    print("your dice number is  :" , dicenum)

else:
    print ("Sorry! maybe next time")
