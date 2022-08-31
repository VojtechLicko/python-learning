from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
          'King': 10, 'Ace': 11}


class Card():
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck():
    def __init__(self) -> None:
        self.deck = []
        for suit in suits:
            for rank in ranks:
                output_card = Card(suit, rank)
                self.deck.append(output_card)

    def __str__(self) -> str:
        all_cards = ""
        for card in self.deck:
            all_cards += card.__str__() + "\n"
        return all_cards

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand():
    def __init__(self) -> None:
        self.cards = []
        self.aces = 0
        self.value = 0

    def add_card(self, deck):
        current_card = deck.deal()
        if current_card.value == 11 and (self.value + 11) > 21:
            self.aces += 1
            self.value += 1
            # print("Ace found, value adjusted")
        else:
            self.value += current_card.value
        self.cards.append(current_card)

    def __str__(self) -> str:
        all_cards_hand = ""
        for card in self.cards:
            all_cards_hand += card.__str__() + "\n"
        return all_cards_hand


class Chips():
    def __init__(self, starting_amount) -> None:
        self.starting_amount = starting_amount

    def bet_chips(self):
        while True:
            try:
                bet_amount = int(
                    input("Enter the amount you would like to bet :"))
                if bet_amount > self.starting_amount:
                    print(
                        "U have to enter a bet amount that is less than your current balance")
                    raise TypeError
                break
            except ValueError:
                print("U have to enter whole number")
                continue
            except TypeError:
                continue
        return bet_amount

    def lose_chips(self, bet):
        self.starting_amount -= bet
        # return self.starting_amount

    def win_chips(self, bet):
        self.starting_amount += bet
        # return self.starting_amount

    def __str__(self) -> str:
        return "Current number of chips :" + str(self.starting_amount)


def show_some(player_hand, dealer_hand):
    print("\nDealer hand : ")
    print(dealer_hand.cards[0])
    print("<card hidden>")
    print("Dealers card value <value hidden>")
    print("\n Player hand :")
    print(*player_hand.cards, sep="\n")
    print(f"Player card value {player_hand.value}")


def show_all(player_hand, dealer_hand):
    print("\n Dealer hand : ")
    print(*dealer_hand.cards, sep="\n")
    print(f"Dealers card value {dealer_hand.value}")
    print("\n Player hand :")
    print(*player_hand.cards, sep="\n")
    print(f"Player card value {player_hand.value}")


def hit(hand, deck, dealer_hand, chips):
    while hand.value <= 21:
        show_some(hand, dealer_hand)
        hit_or_stand = input("Do you want to hit or stand ?")
        if hit_or_stand[0].lower() == "h":
            hand.add_card(deck)
            if hand.value > 21:
                show_all(hand, dealer_hand)
                print("Player busts !")
                chips.lose_chips(bet)
                print(chips)
                break
            else:
                continue
        else:
            while dealer_hand.value < 17:
                dealer_hand.add_card(deck)
            if dealer_hand.value > 21:
                show_all(hand, dealer_hand)
                print("Dealer busts !")
                chips.win_chips(bet)
                print(chips)
                break
            elif 17 <= dealer_hand.value <= 21:
                if dealer_hand.value == player_hand.value:
                    show_all(hand, dealer_hand)
                    print("Its a tie !")
                    print(chips)
                    break
                elif dealer_hand.value > player_hand.value:
                    show_all(hand, dealer_hand)
                    print("Dealer wins !")
                    chips.lose_chips(bet)
                    print(chips)
                    break
                elif player_hand.value > dealer_hand.value:
                    show_all(hand, dealer_hand)
                    print("Player wins")
                    chips.win_chips(bet)
                    print(chips)
                    break


while True:
    keep_playing = True
    while True:
        try:
            chip_amount = int(
                input("Enter the amount of chips you would like to start with :"))
            break
        except ValueError:
            print("U have to enter whole number")
            continue
    my_chips = Chips(chip_amount)
    while keep_playing:
        bet = my_chips.bet_chips()

        my_deck = Deck()
        my_deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(my_deck)
        player_hand.add_card(my_deck)

        dealer_hand = Hand()
        dealer_hand.add_card(my_deck)
        dealer_hand.add_card(my_deck)

        hit(player_hand, my_deck, dealer_hand, my_chips)
        if my_chips.starting_amount <= 0:
            print("You are out of chips")
            break
        keep_playing = input("Do you want to keep playing ? (no/yes)")
        if keep_playing[0].lower() == "n":
            keep_playing = False

    break
