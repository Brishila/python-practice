from Card import Card
import random

class Deck(Card):
    def __init__(self, suits, ranks):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_of_cards = ''
        for card in self.deck:
            deck_of_cards += card.__str__()
        return (f'Deck has {deck_of_cards}')

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card



