#task: create a head and tail program using random module. If it is 1 then head otherwise tail (0)
import random

headOrTaile = random.randint(0,1)
if headOrTaile == 1:
    print("Head")
else:
    print('Tails')