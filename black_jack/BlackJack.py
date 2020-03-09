from Card import Card
from Deck import Deck
from Hand import Hand
from Chip import Chip

global playing 
playing = True
class BlackJack:

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    
    show = False

    def show_card(self, dealer_hand, player_hand):
        print('Dealers Hand')
        if self.show:
            for dealer_card in dealer_hand.card:
                print(f' {dealer_card}')
        else:
            print(' <card hidden>')
            print(f' {dealer_hand.card[1]}')
        
        print('Players Hand')
        for player_card in player_hand.card:
            print(f' {player_card}')

    def get_bet(self):
        while True:
            try:
                bet_chips = int(input('How many chips would you like to bet ?'))
                chips = Chip()
                if bet_chips > chips.total:
                    print(f'You have {chips.total}, Please enter valid number')
                else:
                    return bet_chips
            except:
                print('Invalid number')
                continue

    def player_busts(self, player_hand):
        if player_hand.value < 21:
            print(player_hand.value)
            return False
        else:
            print(player_hand.value)
            return True

    def dealer_busts(self, dealer_hand):
        if dealer_hand.value < 17:
            print(dealer_hand.value)
            return False
        else:
            print(dealer_hand.value)
            return True 

    def check_win(self, dealer_hand, player_hand):
        if dealer_hand.value == 17 and dealer_hand.value > player_hand.value:
            return {'dealer':True, 'player':False}
        elif player_hand.value > dealer_hand.value:
            return {'dealer':False, 'player':True}
        else:
            return {'dealer':False, 'player':False}
    
    def replay(self):
        while True:
            try:
                replay_flag = input('Would you like to play agian(y/n) ?').upper()
                if replay_flag == 'Y':
                    return True
                elif replay_flag == 'N':
                    return False
                else:
                    print('Please enter (y/n)')
                    continue
            except:
                print('Invalid input')
                continue

if __name__ == "__main__":
    print('Welcome to BlackJack! Get as close to 21 as you can without going over! \
        \n Dealer hits until she reaches 17. Aces count as 1 or 11.')

    while playing:
        blackjack = BlackJack()
        bet_chips = blackjack.get_bet()
        deck_object = Deck(BlackJack.suits, BlackJack.ranks)
        deck_object.shuffle()

        dealer_hand = Hand()
        dealer_hand.add_card(deck_object.deal())
        dealer_hand.add_card(deck_object.deal())

        player_hand = Hand()
        player_hand.add_card(deck_object.deal())
        player_hand.add_card(deck_object.deal())
        
        blackjack.show_card(dealer_hand, player_hand)
        result = blackjack.check_win(dealer_hand, player_hand)

        while True:
            try:
                hit_stand = input('Hit or stand(h/s)?').lower()
                if hit_stand == 'h':
                    if not blackjack.player_busts(player_hand):
                        player_hand.add_card(deck_object.deal())
                        dealer_hand.add_card(deck_object.deal())
                    else:
                        print('Player busted')
                elif hit_stand == 's':
                    if not blackjack.dealer_busts(dealer_hand):
                        dealer_hand.add_card(deck_object.deal())
                    else:
                        print('Dealer busted')
                else:
                    print('Enter valid response(h/s)')
                    continue
                print(blackjack.check_win(player_hand, dealer_hand))
                break
            except:
                print('Enter valid response (h/s)')
                continue
            
        if not blackjack.replay():
            print('Thank you!')
            playing = False