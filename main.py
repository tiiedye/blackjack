# Blackjack Project - Our Blackjack House Rules

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from art import logo

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


def deal_card():
    return random.choice(cards)


def calculate_score(hand):
    score = 0

    if "A" in hand:
        hand.remove("A")
        hand.append("A")

    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            score += 10
        elif card == "A" and score + 11 <= 21:
            score += 11
        elif card == "A" and score + 11 >= 21:
            score += 1
        else:
            score += card

    return score


print(logo)
print("RULES:")
print("1. The deck is unlimited in size.\n 2. There are no jokers.\n 3. The Jack/Queen/King all count as 10.\n 4. The "
      "the Ace can count as 11 or 1.\n 5. Cards marked X are face down\n")

user_cards = []
dealer_cards = []

user_cards.append(deal_card())
user_cards.append(deal_card())
dealer_cards.append(deal_card())
dealer_cards.append(deal_card())

print("Your cards:")
print(f"{user_cards}")
user_score = calculate_score(user_cards)
print(f"Your total: {user_score}\n")

print("Dealer's cards:")
print(f"[ {dealer_cards[0]}, X ]")

hit_or_pass = "h"
while hit_or_pass == 'h':
    hit_or_pass = input("Would you like to Hit [H] or Pass [P]?: ").lower()
    if hit_or_pass == 'h':
        user_cards.append(deal_card())
    elif hit_or_pass != 'h' and hit_or_pass != 'p':
        print("Invalid input, pass assumed.")

print("Your cards:")
print(f"{user_cards}")
user_score = calculate_score(user_cards)
print(f"Your total: {user_score}\n")

print("Dealer's cards:")
print(f"{dealer_cards}")
dealer_score = calculate_score(dealer_cards)
print(f"Dealer's total: {dealer_score}")
