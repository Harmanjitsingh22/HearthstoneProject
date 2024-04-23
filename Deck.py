# Name : HARMANJIT SINGH
# Student no. : 300212091
# UFV email  : harmanjit.singh2@student.ufv.ca

from Card import Card
from Creature import Creature
from Resource import Resources
from Equipment import Equipment
from Spell import Spell

import random

class Deck(Card):
    # Each player gets a deck of 20 cards
    def __init__(self):
        self.cards = [] # create a empty list of cards
        

    # Each deck consists of the following cards:
    # 8 resources
    # 8 creatures
    # 2 spells (one of each)
    # 2 equipment (one of each)

    def shuffle(self):
        random.shuffle(self.cards)

    # could be the __init__()
    def create_deck(self): 
        self.cards=[]
        # Create 8 Creature cards
        for card_number in range(8):
            names = ["Fiery dragon", "Poison Dragon", "Earth dragon", "Water dragon","Storm Dragon", "Air dragon", "Ice dragon", "Thunder Dragon"]
            attacks = [1,1,2,2,3,3,4,4]
            defenses = [1,2,1,2,1,2,1,2]
            cost_of_creature_cards =[1,1,2,2,3,3,4,4]
            self.new_creature = Creature(names[card_number], attacks[card_number], defenses[card_number], cost_of_creature_cards[card_number])
            self.cards.append(self.new_creature)

        # Create 8 Resource cards
        for card_number in range(8):
            names = [" 1 Gold coins", " 1 Gold coins", " 2 Gold coins"," 3 Gold coins"," 1 Gold coins"," 2 Gold coins"," 4 Gold coins "," 2 Gold coins"]
            value = [1,1,2,3,1,2,4,2]
            self.resource_card_only = Resources(names[card_number], value[card_number],0)
            self.cards.append(self.resource_card_only )

        # Create 2 Equipment card
        for card_number in range(2):
            names = ["Sword" , "Shield"]
            resource_cost =[2,5]
            self.equipment_card_only = Equipment(names[card_number], "Equipment", resource_cost[card_number] )
            self.cards.append(self.equipment_card_only )

        # Create 2 Spell card
        for card_number in range(2):
            names = ["Heal" , "Fireball", "Destroy creature"]
            resource_cost=[2, 2, 4]
            self.spell_card_only = Spell( names[card_number],"Spell", resource_cost[card_number])
            self.cards.append(self.spell_card_only )

        pass

    def draw_card_from_deck(self, name):
        if len(self.cards) > 0:
            self.shuffle()
            drawn_card = self.cards[0]
            print(f"{name} drew a {drawn_card.name} {drawn_card.card_type} card from the deck.")
            self.cards.remove(drawn_card)
            return drawn_card
        else:
            print("Deck is empty.")
            return None