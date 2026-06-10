import random
import art

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw(k, any_list):
    any_list.extend(random.choices(deck, k=k))

def score(any_list):
    return sum(any_list)

def compute(player_list, dealer_list):
    ask_again = input("Type y to get another card, type n to pass: ")
    if ask_again == "y":
        draw(1, player_list)
        print(f"      Your cards: {player_list}, current score: {score(player_list)}")
        return None  # continue the game
    else:
        # dealer draws until 17 — AFTER loop compare
        while score(dealer_list) < 17:
            draw(1, dealer_list)

        # compare AFTER dealer finishes drawing
        if score(dealer_list) > 21:
            return "you win — dealer went over 21"
        elif score(player_list) > score(dealer_list):
            return "you win"
        elif score(player_list) < score(dealer_list):
            return "you lose"
        else:
            return "its a draw"

def blackjack():
    player_list = []
    dealer_list = []
    print(art.logo)
    draw(2, player_list)
    draw(2, dealer_list)
    print(f"      Your cards: {player_list}, current score: {score(player_list)}")
    print(f"      Computer's first card: {dealer_list[0]}")

    while True:
        if score(player_list) == 21 and len(player_list) == 2:
            return "you win!!! blackjack"
        elif score(dealer_list) == 21 and len(dealer_list) == 2:
            return "you lose!!! dealer has blackjack"

        if score(player_list) > 21:
            if 11 in player_list:
                x = player_list.index(11)
                player_list[x] = 1
                if score(player_list) > 21:
                    return "you lose"
                    # if ace fix helped, continue loop
            else:
                return "you lose"
        else:
            result = compute(player_list, dealer_list)
            if result is not None:  # None means player hit, keep going
                return result

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    print(blackjack())
