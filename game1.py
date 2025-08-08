# snake water gun 
import random
def gamewin(comp , you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False
        
print("Comp Turn : Snake(s), Water(w), Gun(g) ?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you= input("Your Turn: Snake(s), Water(w),and Gun(g) ?\n")
a=gamewin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose:{you}")

if a==None:
    print("The Game is Tie!")
elif a:
    print("You win !")
else:
    print("You lose!")