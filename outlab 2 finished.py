###October 2nd 2018
###Justin Guerrero
###Outlab 2
### --------------------------------------

##import what we need to make it work
import random
import math


def print_hand(hand_list):
    print("Cribbage Hand")
    print("-------------")
    for i in range(0,3):
        print("Card " + str(i +1) + ": " + str(hand_list[i][0]) + " of " + str(hand_list[i][1]))
    #print("card 1", hand_list[0][0],"of", hand_list[0][1])

##here we evaluate points for the hand
        
def evaluate_hand(hand_list):
    score = 0
    card1 = hand_list[0]
    card2 = hand_list[1]
    card3 = hand_list[2]
    
    card_list = [card1[0], card2[0], card3[0]]
    
    score = score + three_o_kind(card_list)
    score = score + pair(card_list)
    score = score + sequence(card_list)
    score = score + fifteen(card_list)
    print("Your score is", score)
    
## Here we will define the scoring bracket

def three_o_kind(card_list):
    if card_list[0] == card_list[1] == card_list[2]:
        return 6
    else:
        return 0
def pair(card_list):
    if card_list[0] == card_list[1] and card_list[1] != card_list[2]:
        return 2
    elif card_list[0] == card_list[2] and card_list[0] != card_list[1]:
        return 2
    elif card_list[1] == card_list[2] and card_list[1] != card_list[0]:
        return 2
    else:
        return 0

    
def fifteen(card_list):
    if card_list[0] + card_list[1] == 15:
        return 2
    elif card_list[0] + card_list[2] == 15:
        return 2
    elif card_list[1] + card_list[2] == 15:
        return 2
    elif card_list[0] + card_list[1] + card_list[2] == 15:
        return 2
    else:
        return 0

    
def sequence(card_list):
    card_list.sort()

    if card_list[0] + 1 and card_list[1] + 1 == card_list[2]:
        return 3
    else:
        return 0

##here is the given code
    
def process_hands(cribbage_input, cards_in_hand):    

    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([int(hand[0]), hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list)
        evaluate_hand(hand_as_list)
4
# --------------------------------------

def main():
    cribbage_file= open("cribbage.txt", "r")
    process_hands(cribbage_file, 3)
    cribbage_file.close()

# --------------------------------------

main()






