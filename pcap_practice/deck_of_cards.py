import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    
    def present(self):
        return self.value + " of " + self.suit

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for i in suits:
            for j in values:
                self.cards.append(Card(i,j))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop(-1)
    
    def count_remaining(self):
        return len(self.cards)

    def get_reamining(self):
        string_list = []
        for i in self.cards:
            string_list.append(i.present())
        return string_list

new_deck = Deck()
new_deck.shuffle()
print(new_deck.deal().present())
print(new_deck.count_remaining())
print(new_deck.get_reamining())