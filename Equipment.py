# Name : HARMANJIT SINGH
# Student no. : 300212091
# UFV email  : harmanjit.singh2@student.ufv.ca

from Card import Card


class Equipment(Card):
    def __init__(self, name=None, card_type=None, resource_cost=None):
        super().__init__(name, card_type, resource_cost)
        self.card_type = card_type
        self.equipment_name = name

    def set_equipment_type(self, card_type):
        self.equipment_type = card_type