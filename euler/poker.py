from itertools import groupby

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
card_suits = ['H', 'S', 'C', 'D']

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIRS = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH= 8
ROYAL_FLUSH = 9

def value(card):
    return card[0]

def suit(card):
    return card[1]

def pos_value(card):
    return card_values[value(card)]

def group_cards_by_value(hand):
    sorted_cards = sorted(hand, key=pos_value)
    final_dict = {}
    for k, v in groupby(sorted_cards, key=value):
        final_dict.update({k: list(v)})
    return final_dict

def group_cards_by_suit(hand):
    sorted_cards = sorted(hand, key=suit)
    final_dict = {}
    for k, v in groupby(sorted_cards, key=suit):
        final_dict.update({k: list(v)})
    return final_dict

def one_pair(hand):
    grouped_hand = group_cards_by_value(hand)
    groups = list(grouped_hand.values())
    pairs = list(filter(lambda g: len(g) == 2, groups))
    return ONE_PAIR if (len(pairs) == 1) else -1

def two_pairs(hand):
    grouped_hand = group_cards_by_value(hand)
    groups = list(grouped_hand.values())
    pairs = list(filter(lambda g: len(g) == 2, groups))
    return TWO_PAIRS if (len(pairs) == 2) else -1

def three_of_a_kind(hand):
    grouped_hand = group_cards_by_value(hand)
    groups = list(grouped_hand.values())
    triples = list(filter(lambda g: len(g) == 3, groups))
    return THREE_OF_A_KIND if (len(triples) == 1) else -1

def four_of_a_kind(hand):
    grouped_hand = group_cards_by_value(hand)
    groups = list(grouped_hand.values())
    quartet = list(filter(lambda g: len(g) == 4, groups))
    return FOUR_OF_A_KIND if len(quartet) == 1 else -1

def flush(hand):
    grouped_hand = list(group_cards_by_suit(hand).values())
    return FLUSH if (len(grouped_hand) == 1) else -1

def straight(hand):
    values, suits = list(zip(*[list(card) for card in hand]))
    new_values = [card_values[v1] for v1 in values]
    new_values.sort()
    val_set = set()
    val_set.update(new_values)
    return STRAIGHT if (new_values[-1] - new_values[0] == 4 and len(val_set) == 5) else -1

def full_house(hand):
    return FULL_HOUSE if (one_pair(hand) > 0 and three_of_a_kind(hand) > 0) else -1

def straight_flush(hand):
    return STRAIGHT_FLUSH if (straight(hand) > 0 and flush(hand) > 0) else -1

def royal_flush(hand):
    values, suits = list(zip(*[list(card) for card in hand]))
    new_values = [card_values[v1] for v1 in values]
    min_value = min(new_values)
    return ROYAL_FLUSH if ((min_value == 10) and straight_flush(hand) > 0) else -1

def get(hand):
    return [
        0,
        one_pair(hand),
        two_pairs(hand),
        three_of_a_kind(hand),
        straight(hand),
        flush(hand),
        full_house(hand),
        four_of_a_kind(hand),
        straight_flush(hand),
        royal_flush(hand)
    ]

# Should return the pairs a hand has
def get_pairs(hand):
    groups = group_cards_by_value(hand)
    l = []
    for k in groups.keys():
        if len(groups[k]) > 1:
            l.append(groups[k])
    return l

def break_tie(hand1, hand2, tie):
    if tie == HIGH_CARD:
        return high_card(hand1, hand2)
    elif tie == ONE_PAIR:
        p1, p2 = get_pairs(hand1), get_pairs(hand2)
        return high_card(p1[0], p2[0])

# Here we assume that nobody has a 'relevant' hand, so
# we break the tie based on the highest card they have:
def high_card(hand1, hand2):
    max_v1 = max(list(map(pos_value, hand1)))
    max_v2 = max(list(map(pos_value, hand2)))
    return max_v1 > max_v2