from Variables import Variables
from Deck import Deck
from Hand import Hand

v = Variables()


test_deck = Deck(v.get_suits(), v.get_ranks(), v.get_values())
test_deck.shuffle()
test_player = Hand(v.get_values())
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print(test_player.value)
for card in test_player.cards:
    print(card)