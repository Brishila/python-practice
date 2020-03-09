class Hand:

    
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
            'Queen':10, 'King':10, 'Ace':11}

    def __init__(self):
        self.card = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.card.append(card)
        self.value += self.values[card.rank]

    def adjust_for_ace(self):
        for card in self.card:
            if card.rank == 'Ace' and self.value > 21:
                self.value -= 10
                