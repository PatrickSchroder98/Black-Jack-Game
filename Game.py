from Variables import Variables
from Deck import Deck
from Hand import Hand
from Chips import Chips
from Engine import Engine

class Game:
    v = Variables()
    e = Engine()

    def main_loop(self):
        while True:
            print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')
            playing = True
            deck = Deck(self.v.get_suits(), self.v.get_ranks(), self.v.get_values())
            deck.shuffle()

            player_hand = Hand(self.v.get_values())
            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())

            dealer_hand = Hand(self.v.get_values())
            dealer_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

            player_chips = Chips()

            self.e.take_bet(player_chips)

            self.e.show_some(player_hand, dealer_hand)

            while playing:

                playing = self.e.hit_or_stand(deck, player_hand)

                self.e.show_some(player_hand, dealer_hand)

                if player_hand.value > 21:
                    self.e.player_busts(player_hand, dealer_hand, player_chips)
                    break

            if player_hand.value <= 21:

                while dealer_hand.value < 17:
                    self.e.hit(deck, dealer_hand)

                self.e.show_all(player_hand, dealer_hand)

                if dealer_hand.value > 21:
                    self.e.dealer_busts(player_hand, dealer_hand, player_chips)

                elif dealer_hand.value > player_hand.value:
                    self.e.dealer_wins(player_hand, dealer_hand, player_chips)

                elif dealer_hand.value < player_hand.value:
                    self.e.player_wins(player_hand, dealer_hand, player_chips)

                else:
                    self.e.push(player_hand, dealer_hand)

            print("\nPlayer's winnings stand at", player_chips.total)

            new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

            if new_game[0].lower() == 'y':
                playing = True
                continue
            else:
                print("Thanks for playing!")
                break