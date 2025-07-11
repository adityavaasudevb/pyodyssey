rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_list=[rock,paper,scissors]
a=int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))
print(rps_list[a])

import random
rps_random=random.randint(0,2)
print(f"Computer chose:\n{rps_list[rps_random]}")

'''
if a==0:
    if rps_random==1:
        print("You lose")
    elif rps_random==2:
        print("You Win")
    else:
        print("Its a draw")
if a==1:
    if rps_random==2:
        print("You lose")
    elif rps_random==0:
        print("You Win")
    else:
        print("Its a draw")
if a==2:
    if rps_random==0:
        print("You lose")
    elif rps_random==1:
        print("You Win")
    else:
        print("Its a draw")
'''
if a<0 and a>2:
    print("Invalid choice")
else:
    if a==rps_random:
        print("It's a draw.")
    elif a==0 and rps_random==2:
        print("You win")
    elif a==2 and rps_random==0:
        print("You lose")
    elif a>rps_random:
        print("You win")
    elif a<rps_random:
        print("You lose")




