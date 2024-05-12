import sys

def card_value(value):
    if value == 'A':
        return 0
    elif value == 'T':
        return 9
    elif value == 'J':
        return 10
    elif value == 'Q':
        return 11
    elif value == 'K':
        return 12
    else:
        return int(value) - 1

def hand_value(flush):
    values = []
    hand_value = None
    last = hand[0]
    straight = True

    if not last:
        if hand[4] == 12:
            for i in range(4):
                if hand[i] - 1 != hand[i + 1]:
                    if hand[i] > 8:
                        straight = False
                    elif hand[i] < 8 and hand[i + 1] >= 8 and i != hand[i] + 1:
                        straight = False
        else:
            straight = False
    else:
        for i in range(4):
            if hand[i] + 1 != hand[i + 1]:
                straight = False

    if straight and flush:
        values = [13 if card == 0 else card for card in hand]
        values.sort()
        hand_value = 8
    else:
        current_cards = 0
        four_kind = False
        full_house = False
        third = False
        pair = False
        two_pair = False

        for i in range(13):
            if frequence[i] == 4:
                four_kind = True
            elif frequence[i] == 3:
                if pair:
                    full_house = True
                else:
                    third = True
                current_cards += 3
            elif frequence[i] == 2:
                if third:
                    full_house = True
                elif pair:
                    two_pair = True
                else:
                    pair = True
                current_cards += 2

        current_cards = 0

        if four_kind:
            values = [0] * 2
            for i in range(13):
                if frequence[i] == 4:
                    current_cards += 4
                    values[1] = 13 if i == 0 else i
                elif frequence[i] == 1:
                    current_cards += 1
                    values[0] = 13 if i == 0 else i
            hand_value = 7
        elif full_house:
            values = [0] * 2
            for i in range(13):
                if frequence[i] == 3:
                    current_cards += 3
                    values[1] = 13 if i == 0 else i
                elif frequence[i] == 2:
                    current_cards += 2
                    values[0] = 13 if i == 0 else i
            hand_value = 6
        elif flush:
            values = [13 if card == 0 else card for card in hand]
            values.sort()
            hand_value = 5
        elif straight:
            values = [13 if card == 0 else card for card in hand]
            values.sort()
            hand_value = 4
        elif third:
            values = [0] * 3
            j = 0
            for i in range(13):
                if frequence[i] == 3:
                    current_cards += 3
                    values[2] = 13 if i == 0 else i
                elif frequence[i] == 1:
                    current_cards += 1
                    values[j] = 13 if i == 0 else i
                    j += 1
            values.sort()
            hand_value = 3
        elif two_pair:
            values = [0] * 3
            j = 1
            for i in range(13):
                if frequence[i] == 2:
                    current_cards += 2
                    values[j] = 13 if i == 0 else i
                    j += 1
                elif frequence[i] == 1:
                    current_cards += 1
                    values[0] = 13 if i == 0 else i
            values.sort()
            hand_value = 2
        elif pair:
            values = [0] * 4
            j = 0
            for i in range(13):
                if frequence[i] == 2:
                    current_cards += 2
                    values[3] = 13 if i == 0 else i
                elif frequence[i] == 1:
                    current_cards += 1
                    values[j] = 13 if i == 0 else i
                    j += 1
            values.sort()
            hand_value = 1
        else:
            values = [13 if card == 0 else card for card in hand]
            values.sort()
            hand_value = 0

    return hand_value, values

if __name__ == "__main__":
    values = []
    frequence = [0] * 13
    for line in sys.stdin:
        hand = []
        for card in line.strip().split():
            value, suit = card[:-1], card[-1]
            hand.append(card_value(value))
            frequence[hand[-1]] += 1
            if suit != line.strip().split()[0][-1]:
                flush = False
        hand.sort()
        hand_value_white, values_white = hand_value(flush)
        hand.clear()
        for card in input().strip().split():
            value, suit = card[:-1], card[-1]
            hand.append(card_value(value))
            frequence[hand[-1]] += 1
            if suit != input().strip().split()[0][-1]:
                flush = False
        hand.sort()
        hand_value_black, values_black = hand_value(flush)
        if hand_value_white < hand_value_black:
            print("White wins.")
        elif hand_value_white > hand_value_black:
            print("Black wins.")
        else:
            tie = True
            for i in range(len(values_white) - 1, -1, -1):
                if values_white[i] < values_black[i]:
                    print("White wins.")
                    tie = False
                    break
                elif values_white[i] > values_black[i]:
                    print("Black wins.")
                    tie = False
                    break
            if tie:
                print("Tie.")


import sys

def card_value(value):
    if value == 'A':
        return 0
    elif value == 'T':
        return 9
    elif value == 'J':
        return 10
    elif value == 'Q':
        return 11
    elif value == 'K':
        return 12
    else:
        return int(value) - 1

def hand_value(flush):
    values = []
    hand_value = None
    last = hand[0]
    straight = True

    if not last:
        if hand[4] == 12:
            for i in range(4):
                if hand[i] - 1 != hand[i + 1]:
                    if hand[i] > 8:
                        straight = False
                    elif hand[i] < 8 and hand[i + 1] >= 8 and i != hand[i] + 1:
                        straight = False
        else:
            straight = False
    else:
        for i in range(4):
            if hand[i] + 1 != hand[i + 1]:
                straight = False

    if straight and flush:
        values = [13 if card == 0 else card for card in hand]
        values.sort()
        hand_value = 8
    else:
        current_cards = 0
        four_kind = False
        full_house = False
        third = False
        pair = False
        two_pair = False

        for i in range(13):
            if frequence[i] == 4:
                four_kind = True
            elif frequence[i] == 3:
                if pair:
                    full_house = True
                else:
                    third = True
                current_cards += 3
            elif frequence[i] == 2:
                if third:
                    full_house = True
                elif pair:
                    two_pair = True
                else:
                    pair = True
                current_cards += 2

        current_cards = 0

        if four_kind:
            values = [0] * 2
            for i in range(13):
                if frequence[i] == 4:
                    current_cards += 4
                    values[1] = 13 if i == 0 else i
                elif frequence[i] == 1:
                    current_cards += 1
                    values[0] = 13 if i == 0 else i
            hand_value = 7
        elif full_house:
            values = [0] * 2
            for i in range(13):
                if frequence[i] == 3:
                    current_cards += 3
                    values[1] = 13 if i == 0 else i
                elif frequence[i] == 2:
                    current_cards += 2
                    values[0] = 13 if i == 0 else i
            hand_value = 6
        elif flush:
            values = [13 if card == 0 else card for card in hand]
            values.sort()
            hand_value = 5
        elif straight:
            values = [13 if card == 0 else card for card in hand]
            values.sort()
            hand_value = 4
        elif third:
            values = [0] * 3
            j = 0
            for i in range(13):
                if frequence[i] == 3:
                    current_cards += 3
                    values[2] = 13 if i == 0 else i
                elif frequence[i] == 1:
                    current_cards += 1
                    values[j] = 13 if i == 0 else i
                    j += 1
            values.sort()
            hand_value = 3
        elif two_pair:
            values = [0] * 3
            j = 1
            for i in range(13):
                if frequence[i] == 2:
                    current_cards += 2
                    values[j] = 13 if i == 0 else i
                    j += 1
                elif frequence[i] == 1:
                    current_cards += 1
                    values[0] = 13 if i == 0 else i
            values.sort()
            hand_value = 2
        elif pair:
            values = [0] * 4
            j = 0
            for i in range(13):
                if frequence[i] == 2:
                    current_cards += 2
                    values[3] = 13 if i == 0 else i
                elif frequence[i] == 1:
                    current_cards += 1
                    values[j] = 13 if i == 0 else i
                    j += 1
            values.sort()
            hand_value = 1
        else:
            values = [13 if card == 0 else card for card in hand]
            values.sort()
            hand_value = 0

    return hand_value, values

if __name__ == "__main__":
    values = []
    frequence = [0] * 13
    for line in sys.stdin:
        hand = []
        for card in line.strip().split():
            value, suit = card[:-1], card[-1]
            hand.append(card_value(value))
            frequence[hand[-1]] += 1
            if suit != line.strip().split()[0][-1]:
                flush = False
        hand.sort()
        hand_value_white, values_white = hand_value(flush)
        hand.clear()
        for card in input().strip().split():
            value, suit = card[:-1], card[-1]
            hand.append(card_value(value))
            frequence[hand[-1]] += 1
            if suit != input().strip().split()[0][-1]:
                flush = False
        hand.sort()
        hand_value_black, values_black = hand_value(flush)
        if hand_value_white < hand_value_black:
            print("White wins.")
        elif hand_value_white > hand_value_black:
            print("Black wins.")
        else:
            tie = True
            for i in range(len(values_white) - 1, -1, -1):
                if values_white[i] < values_black[i]:
                    print("White wins.")
                    tie = False
                    break
                elif values_white[i] > values_black[i]:
                    print("Black wins.")
                    tie = False
                    break
            if tie:
                print("Tie.")

#Sample Input
#2H 3D 5S 9C KD 2C 3H 4S 8C AH
#2H 4S 4C 2D 4H 2S 8S AS QS 3S
#2H 3D 5S 9C KD 2C 3H 4S 8C KH
#2H 3D 5S 9C KD 2D 3H 5C 9S KH

#Sample Output
#White wins.
#Black wins.
#Black wins.
#Tie.