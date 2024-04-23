# Name : HARMANJIT SINGH
# Student no. : 300212091
# UFV email  : harmanjit.singh2@student.ufv.ca

class Card:
    def __init__(self, name="", card_type ="", resource_cost= 0):
        self.card_type = card_type
        self.name = name
        self.card_type = card_type
        self.resource_cost = resource_cost
        
    def set_card_type(self, card_type):
        self.card_type = card_type