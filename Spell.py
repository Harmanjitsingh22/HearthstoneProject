# Name : HARMANJIT SINGH
# Student no. : 300212091
# UFV email  : harmanjit.singh2@student.ufv.ca

from Card import Card

class Spell(Card):
    def __init__(self,  name="", card_type = None, resource_cost= None):
        super().__init__(name, card_type, resource_cost) # one of the two types: block castng of a card or destroy creature

    def set_spell_type(self, card_type):
        self.spell_type = card_type
