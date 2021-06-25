import random
a=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
b=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
c=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game_images=[a,b,c]

d=int(input("enter the number, 0 for rock, 1 for paper and 2 for scissors"))
print("user chose")
user_choice=print(game_images[d])
#if(d==0):
    #print(a)
#if(d==1):
    #print(b)
#if(d==2):
    #print(c)



e=random.randint(0,2)
print("computer chose")
computer_choice=print(game_images[e])
#if(e==0):
    #print(a)
#if(e==1):
    #print(b)
#if(e==2):
    #print(c)
if(d>=3):
    print("invalid number,you lose")
else:


    if(d==0 and e==0):
        print("draw")
    if(d==0 and e==1):
        print("you lose")
    if(d==0 and e==2):
        print("you win")
    if(d==1 and e==0):
        print("you win")
    if(d==1 and e==1):
        print("draw")
    if(d==1 and e==2):
        print("you lose")
    if(d==2 and e==0):
        print("you lose")
    if(d==2 and e==1):
        print("you win")
    if(d==2 and e==2):
        print("draw")

