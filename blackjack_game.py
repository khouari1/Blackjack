__author__ = "Karim Houari"

 # Blackjack game that allows 1 - 4 players to compete against a dealer

import random

number_players = []  # List to hold the number of players for a game


class Player(object):
    """ Player class created as template to create 'player' objects """
    def __init__(self, name):
        self.name = name
        self.list = []
        self.bust = [0]  # If the 'bust' list value is 1 then the player is bust

    def start_game(self):
        """ Runs through the stages for a player until they stand or bust """
        self.list = []
        self.bust[0] = 0
        self.list.append(next(deck))  # Deal initial 2 cards
        self.list.append(next(deck))
        while True:
            player_total = total(self.list)
            player_cards = ", ".join(self.list)
            print "\n%s has these cards [%s] with a total value of %d." % (self.name, player_cards, player_total)
            if player_total > 21:
                print "\n%s is Bust!" % self.name
                self.bust[0] = 1
                break
            elif player_total == 21 and len(self.list) == 2:
                print "\n%s got Blackjack!" % self.name
                break
            elif player_total == 21 and len(self.list) > 2:
                print "\n%s got 21!" % self.name
                break
            else:
                hit_stand = raw_input("\nHit or Stand? (h or s): ").lower()
                while hit_stand not in ['h', 's']:
                    # Validation check that the player's input is either 'h' or 's'
                    print "\nInvalid input. Please enter 'h' or 's'"
                    hit_stand = raw_input("\nHit or Stand? (h or s): ").lower()
                if 'h' in hit_stand:
                    self.list.append(next(deck))
                else:
                    break
        print


class House(object):
    """ # Class House created as template for the 'house' """
    def __init__(self):
        self.list = []
        self.bust = [0]

    def start_house(self, *args):
        """ Runs through the stages of the game and results in either player(s) or the house winning"""
        self.list = []
        house_total = total(self.list)
        house_cards = ", ".join(self.list)
        while True:
            house_total = total(self.list)
            house_cards = ", ".join(self.list)
            if house_total < 17:
                self.list.append(next(deck))
            else:
                break
        print "The House has these cards [%s] with a total value of %d." % (house_cards, house_total) + "\n"
        if house_total > 21 and self.bust[0] == 0:
            print "The House is bust!" + "\n"
        for i in args:  # Loop through each item in args (arguments)
            if house_total > 21:
                if i.bust[0] is 0:
                    print "%s wins!" % i.name
                else:
                    print "%s loses!" % i.name
            elif house_total == total(i.list):
                if house_total == total(i.list) and total(i.list) == 21 and len(i.list) == 2:
                    print "%s wins with Blackjack!" % i.name
                else:
                    print "%s loses because it was a tie!" % i.name
            elif total(i.list) > house_total:
                if total(i.list) > house_total and i.bust[0] is 0:
                    print "%s wins with a total greater than the House!" % i.name
                else:
                    print "%s loses because they are bust!" % i.name
            elif house_total > total(i.list):
                if house_total > total(i.list):
                    print "%s loses with a score lower than the House!" % i.name
        print


def how_many_players():
    """ Ask how many players for current game """
    del number_players[:]  # Deletes content of 'number_players' list to append a new choice if the player plays again
    number_choice = raw_input("\nEnter number of human players (1 - 4): ")
    while number_choice not in ['1', '2', '3', '4']:
        # Validation check to ensure number_choice is a number between 1 and 4
        print "\nInvalid input. Please enter a number between 1 and 4."
        number_choice = raw_input("\nEnter number of human players (1 - 4): ")
    number_players.append(int(number_choice))


def get_deck():
    """ Get a new deck """
    deck = [value + suit for value in '23456789TJQKA' for suit in 'SHDC']
    random.shuffle(deck)  # Puts cards in deck in random order
    return iter(deck)


def play():
    """ Set up the requested number of players for the game """
    how_many_players()
    if number_players[0] == 1:
        Player.start_game(player1)
        House.start_house(house, player1)
    elif number_players[0] == 2:
        Player.start_game(player1)
        Player.start_game(player2)
        House.start_house(house, player1, player2)
    elif number_players[0] == 3:
        Player.start_game(player1)
        Player.start_game(player2)
        Player.start_game(player3)
        House.start_house(house, player1, player2, player3)
    elif number_players[0] == 4:
        Player.start_game(player1)
        Player.start_game(player2)
        Player.start_game(player3)
        Player.start_game(player4)
        House.start_house(house, player1, player2, player3, player4)  # Example of House taking multiple arguments


def total(hand):
    """ Calculate the total value of a hand """
    hand = ''.join(hand)  # Joins all the characters into one string
    hand = list(hand)  # Divides the individual characters up in a list
    x = sum(int(x) for x in hand if x.isdigit())  # For each item in the hand, if it is a digit then sum them all up
    ace = hand.count('A')  # Count how many 'A' are in the hand
    for i in hand:
        if i == 'T' or i == 'J' or i == 'Q' or i == 'K':
            x += 10
        if i == 'A':
            x += 11
    if x > 21 and ace > 0:
        # If x is > 21 and you have Ace's in your hand, change the Ace's to a value of 1 until x < 22
        while ace > 0 and x > 21:
            x -= 10
            ace -= 1
    return x


def play_again():
    """ Start a new game if the player requests it """
    while True:
        global deck  # Allows a global (outside) variable to be changed inside the function
        deck = get_deck()  # Calls a new deck of cards for the new game
        play()
        ask_user = raw_input("\nWould you like to play again? (y or n): ")
        while ask_user not in ['y', 'n']:
            # Validation of player input - loop if not 'y' or 'n'
            print "\nInvalid input. Please enter 'y' or 'n'"
            ask_user = raw_input("\nWould you like to play again? (y or n): ")
        if ask_user is 'y':
            return True
        elif ask_user == 'n':
            print "\nOk, thanks for playing Blackjack!"
            return False

player1 = Player('Player 1')  # Variables for players 1, 2, 3, and 4 and the House
player2 = Player('Player 2')
player3 = Player('Player 3')
player4 = Player('Player 4')
house = House()
deck = get_deck()  # Global variable assigning the get_deck function to a variable called deck
play_again()  # Call the play_again function which starts the program