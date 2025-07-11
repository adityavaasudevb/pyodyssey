import random
from art import logo


def rand_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def scores(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score=-1
    game_over = False

    for i in range(2):
        user_cards.append(rand_card())
        computer_cards.append((rand_card()))

    while not game_over:
        user_score = scores(user_cards)
        computer_score = scores(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass:")
            if choice == "y":
                user_cards.append(rand_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(rand_card())
        computer_score = scores(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
    print("\n"*20)
    play_game()

'''
import random
from art import logo

input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
# print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = random.sample(cards,2)
computer_cards = random.sample(cards,2)

print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
print(f"Computer's first card: {computer_cards[0]}")

def base_conditions():
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    if sum(computer_cards)==21:
        print("Lose, opponent has Blackjack 😱")

    elif sum(player_cards)==21:
        print("Win with a Blackjack 😎")

    elif sum(player_cards)>21:
        if 11 in player_cards:
            player_cards.remove(11)
            player_cards.append(1)
        else:
            print("You went over. You lose 😭")

flag=True
while flag:
    choice=input("Type 'y' to get another card, type 'n' to pass:")
    if choice=="y":
        player_cards.append(random.choice(cards))
        base_conditions()
    elif choice=="n":
        flag=False


while sum(computer_cards)<17:
    computer_cards.append(random.choice(cards))

player_score=sum(player_cards)
computer_score=sum(computer_cards)
print(f"Your final hand: {player_cards}, final score: {player_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

if sum(computer_cards)>21:
    print("Opponent went over. You win 😁")
else:
    if sum(computer_cards)==sum(player_cards):
        print("Draw 🙃")

    elif sum(computer_cards)>sum(player_cards):
        print("You lose 😤")

    else:
        print("You win 😃")
'''


