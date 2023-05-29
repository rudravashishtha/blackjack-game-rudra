import random
from art import logo
def deal_card():
    cv = {'A': 11, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10}
    card = random.choice(list(cv.keys()))
    return cv[card]

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)


def compare(user_score, com_score):
    if user_score > 21 and com_score > 21:
        return "Score went over. You Lose!"
    
    if user_score == com_score:
        return "Draw!"
    elif com_score == 0:
        return "Lose! Opponent has Blackjack."
    elif user_score == 0:
        return "Congratulations! You Win."
    elif user_score > 21:
        return "You went over! You Lose."
    elif com_score > 21:
        return "Opponent went over! You Win."
    elif user_score > com_score:
        return "Congratulations! You Win."
    else:
        return "You lose!"
    
def play_game():
    # print(logo)
    
    user_cards = []
    computer_cards = []
    game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to hit, 'n' to stand: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)  # Calculate user score after adding a new card
            else:
                game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand: {user_cards}")
    print(f"Computer's final hand: {computer_cards}")
    print(f"Your final score: {user_score}")
    print(f"Computer's final score: {computer_score}")
    print(compare(user_score, computer_score))
            
print(logo)
while input("\nDo you want to play? Type 'y' or 'n': ") == 'y':
    play_game()
