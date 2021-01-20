from art import logo
import random
from replit import clear

# Ace is 11, Jack/Queen/King are 10
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
    # Ace logic (11 -> 1)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11) 
        cards.append(1)
    return sum(cards)

def check_winner(user_score, cpu_score):
    if user_score == cpu_score:
        return 'Draw'
    elif cpu_score == 0:
        return 'Lose, computer has Blackjack'
    elif user_score == 0:
        return 'Win with a Blackjack'
    elif user_score > 21:
        return 'You went over. You lose'
    elif cpu_score > 21:
        return 'Opponent went over. You win'
    elif user_score > cpu_score:
        return 'You win'
    else:
        return 'You lose'

def play_game():
    is_game_over = False
    print(logo)

    # Deal 2 cards for user, cpu
    user_cards = [deal_card() for i in range(2)]
    cpu_cards = [deal_card() for i in range(2)]

    while not is_game_over:
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)
        # Show current status, avoid printing same data twice if user is about to reach game over
        if user_score <= 21:
            print(f'Your cards {user_cards}, current score: {user_score}')
            print(f"Computer's first card: {cpu_cards[0]}")

        # Check if user can add a card
        if user_score == 0 or cpu_score == 0 or user_score > 21 or cpu_score > 21:
            is_game_over = True
        else:  
            # User can add a card
            add_card = input("Type 'y' to get another card. Type 'n' to pass: ").lower()
            if add_card == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True
    # Cpu logic
    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)
    
    # Print final scores and check winner
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {cpu_cards}, final score: {cpu_score}")
    print(check_winner(user_score, cpu_score))

while input("Do you want to play of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    clear()
    play_game()
