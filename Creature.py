# Name : HARMANJIT SINGH
# Student no. : 300212091
# UFV email  : harmanjit.singh2@student.ufv.ca

from Card import Card

class Creature(Card): # a creature is a type of card
    def __init__(self,name = None, attack_strength = None, defense_strength = None, resources_cost= None):
        self.attack_strength = attack_strength
        self.defense_strength = defense_strength
        self.hp = 10                  # Consider initial health points is 10 for simplicity
        super().__init__( name, "Creature", resources_cost)
        self.creature_name = name
        self.resources_cost = resources_cost
    

        