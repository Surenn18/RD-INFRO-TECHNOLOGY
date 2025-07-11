import random
choice=int(input("enter your choice \n1. 0 for rock\n2. 1 for paper\n3. 2 for scissor::"))
computer=random.randint(0,2)
print(f"user choice is {choice}")
print(f"computer choice is{computer}")
if choice==0 or choice==1 or choice==2:
    if choice==computer:
        print("draw the match")
    elif (choice==0 and computer==2) or (choice==2 and computer==1) or (choice==1 and computer==0):
        print("you win")
    else:
        print("you lose")
else:
    print(" please enter the correct choice")
print("bye")