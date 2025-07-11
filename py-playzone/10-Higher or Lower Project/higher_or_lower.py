#import random,logo and data modules
import random
from art import logo,vs
from game_data import data

n=len(data)-1
index1=random.randint(0,n)
index2=random.randint(0,n)

followers1=data[index1]['follower_count']
followers2=data[index2]['follower_count']
result=max(followers1,followers2)
flag=True
c=0

def display(new_index1,new_index2):
    print(logo)
    print(f"Compare A: {data[new_index1]['name']}, a {data[new_index1]['description']}, from {data[new_index1]['country']}.")
    print(vs)
    print(f"Against B: {data[new_index2]['name']}, a {data[new_index2]['description']}, from {data[new_index2]['country']}.")

while flag:
    display(index1,index2)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess=='a' and followers1==result :
        c+=1
        index2=random.randint(0,n)
        print("\n" * 10)
        print(f"You're right! Current score {c}")

    elif guess=='b' and followers2==result:
        c+=1
        index1 = random.randint(0, n)
        print("\n" * 10)
        print(f"You're right! Current score {c}")

    else:
        flag=False
        print("\n" * 10)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {c}.")