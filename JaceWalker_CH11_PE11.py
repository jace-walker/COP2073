# Jace Walker
# This program generates a 52-card deck and assigns/displays 5 cards to the user. They are then prompted to choose
#    cards to replace. The program then replaces the corresponding cards with new ones and displays the new hand.

import random

# create list of numbers on cards (11-14 will correspond to the special cards)
num_list = ['2', '3', '4', '5', '6', '7', '8',
       '9', '10', '11', '12', '13', '14']

# create list of suits
suit_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# create DICTIONARY of the face cards
face_cards = {'11': 'Joker', '12': 'Queen', '13': 'King', '14': 'Ace'}

# create deck class
class Deck:
    def __init__(self, size=1):
        self.card_list = []

# creates 52-card deck
# once generating cards that start with 11, their numerical value is switched to a face card
        for x in range(size):
            for num in num_list:
                display_num = face_cards[num] if num in face_cards else num
                for suit in suit_list:
                    self.card_list.append(f"{display_num} of {suit}")
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

# deal function that assigns user a card
    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card


def main():

# 'deals' 5 cards
    card_deck = Deck()
    for x in range(5):
        print(card_deck.deal())
    print('-----------------')

# prompts user to replace cards
    replaced_cards = input('Enter the cards you want to replace (ex. 3, 4): ')
    if replaced_cards.strip():

# replaces commas
        replaced_cards = replaced_cards.replace(',', ' ')

# creates list out of the now integer input the user provided
        to_replace = [int(card) - 1 for card in replaced_cards.strip().split()]

# reverse the list bc the cards have to be replaced from the highest order otherwise order will mess up
        to_replace = sorted(set(to_replace), reverse=True)
        for replaced in to_replace:
            if 0 <= replaced < len(card_deck.cards_in_play_list):
                card_deck.discards_list.append(card_deck.cards_in_play_list.pop(replaced))

# while user has less than 5 cards, enough to hit 5 will print
    print('Your new cards:')
    while len(card_deck.cards_in_play_list) < 5:
        print(card_deck.deal())

# prints final deck
    print('-----------------')
    print('Your final hand: ')
    for card in card_deck.cards_in_play_list:
        print(card)

# cosmetics
print('Poker Hand Generator')
print('-----------------')
print('Your first hand:')

# call main function
main()
