###October 2nd 2018
###Justin Guerrero
###Outlab 2
### --------------------------------------

##
##
####don't change anything below this line
##
##import what we need to make it work
import random
import math



####define the cards and open file location
##def deck_cards(cards):
##    cribbage_file = open(os.path.join(C:\users\Justin Guerrero\Documents\cs127cribbage.txt))
##    for cards in "ATJQK","123456789":
##        for suits in "DCSH":
##            if cards =='A':
##                return 1
##            elif cards =='T':
##                return 10
##            elif cards =='J':
##                return 10
##            elif cards =='Q':
##                return 10
##            elif cards =='K':
##                return 10

##define card conditions for hand possibilities
##
##card = open(cribbage.txt,r))
##card_number = [card[0], card[2], card[4]]
##sort_card = (sorted(card_number, key=int))
##cond = card[0] + card[2]
##cond1 = card[0] + card[4]
##cond2 = card[2] + card[4]
##cond3 = card[0] + card[2] + card[4]
##cond4 = card[0] == card[2]
##cond5 = card[0] == card[4]
##cond6 = card[2] == card[4]
##cond7 = card[0] == card[2] == card[4]
##cond8 = sort_card[0]+1 == sort_card[1] and sort_card[1]+1 == sort_card[2]
##fifteen_counter = 0
##sequence = 0
##pair = 0
##three_of_a_kind_counter = 0
##def outcomes(card):
##    global three_of_a_kind_counter
##    global sequence
##    global pair
##    global fifteen_counter
##    if cond == 15:
##        fifteen_counter += 1
##    elif cond1 == 15:
##        fifteen_counter += 1
##    elif cond2 == 15:
##        fifteen_counter += 1
##    elif cond3 == 15:
##        fifteen_counter += 1
##    elif cond4 == True:
##        pair += 1
##    elif cond5 == True:
##        pair + 1
##    elif cond6 == True:
##        pair + 1
##    elif cond7 == True:
##        three_of_a_kind_counter +1
##    elif cond8 == True:
##        sequence += 1
##    
#def process_hands(cribbage_input, cards_in_hand):    



def print_hand(hand_list):
    print("Cribbage Hand")
    print("-------------")
    for i in range(0,3):
        print("Card " + str(i +1) + ": " + str(hand_list[i][0]) + " of " + str(hand_list[i][1]))
    #print("card 1", hand_list[0][0],"of", hand_list[0][1])


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
    
def process_hands(cribbage_input, cards_in_hand):    

    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([int(hand[0]), hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list)
        evaluate_hand(hand_as_list)

# --------------------------------------

def main():
    cribbage_file= open("cribbage.txt", "r")
    process_hands(cribbage_file, 3)
    cribbage_file.close()

# --------------------------------------

main()



##
##number = random.randint(0,9)
##number2 = random.randint(1,9)
##number3 = random.randint(1,9)
##suit = ["diamonds", "spades", "clubs", "hearts"]
##card_hand = [number, "suit", number2, "suit", number3, "suit"]






