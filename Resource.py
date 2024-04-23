# Name : HARMANJIT SINGH
# Student no. : 300212091
# UFV email  : harmanjit.singh2@student.ufv.ca

from Card import Card

class Resources(Card):
    def __init__(self,name = None, value = None, resources_cost=None):
        self.value = value
        self.card_type= "Resource"
        super().__init__(name, "Resource", resources_cost)
        self.resources_name = name
        self.resources_cost=resources_cost

    def set_resources_type(self, card_type):
        self.resources_type = card_type
        
        
    