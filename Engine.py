class Engine:

    def take_bet(self, chips):

        while True:
            try:
                chips.bet = int(input('How many chips would you like to bet? '))
            except ValueError:
                print('Sorry, a bet must be an integer!')
            else:
                if chips.bet > chips.total:
                    print("Sorry, your bet can't exceed", chips.total)
                else:
                    break

    def hit(self, deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    def hit_or_stand(self, deck, hand):

        while True:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

            if x[0].lower() == 'h':
                self.hit(deck, hand)

            elif x[0].lower() == 's':
                print("Player stands. Dealer is playing.")
                return False

            else:
                print("Sorry, please try again.")
                continue
            break

    def show_some(self, player, dealer):
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print('', dealer.cards[1])
        print("\nPlayer's Hand:", *player.cards, sep='\n ')

    def show_all(self, player, dealer):
        print("\nDealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =", dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =", player.value)

    def player_busts(self, player, dealer, chips):
        print("Player busts!")
        chips.lose_bet()

    def player_wins(self, player, dealer, chips):
        print("Player wins!")
        chips.win_bet()

    def dealer_busts(self, player, dealer, chips):
        print("Dealer busts!")
        chips.win_bet()

    def dealer_wins(self, player, dealer, chips):
        print("Dealer wins!")
        chips.lose_bet()

    def push(self, player, dealer):
        print("Dealer and Player tie! It's a push.")
