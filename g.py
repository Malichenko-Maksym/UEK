import random
import os
import time
a=random.randrange(1,7)
print(a) #to check
print("I wanna play a game... ")
x=int(input("Guees number from 1 to 6 "))
if a==x:
    print("True")
    input()
else:
    time.sleep(0.1)
    os.system('start Foto.png')