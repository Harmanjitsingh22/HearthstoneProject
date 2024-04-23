# Name : HARMANJIT SINGH
# Student no. : 300212091
# UFV email  : harmanjit.singh2@student.ufv.ca
from Turn import Turn

class Display(Turn):
    def __init__(self):
        pass

    def print_battlefield(self, player1, player2):
        print(f"\n\n Cards in hand of {player2.name}:")
        print('\n'.join([f"\t{card.name}" for card in player2.cards_in_hand]))
        print(f"{player2.name}'s life Total: {player2.life_points}")
        print(f"Resources: { player2.gold} /8\n")
        print(f"\t****Battlefield****\n      =========================\n")
        for card in player2.battlefield:
            if card.card_type=="Creature":
                print((f" {card.name} {card.attack_strength}/{card.defense_strength} (Creature) "), end="\t")
            else:
                print((f" {card.name} {card.resource_cost} ({card.card_type}) "), end="\t")
        print("\n")
        if len(player1.battlefield) >= len(player2.battlefield) and len(player1.battlefield)<=5:
            print(''.join(['--------------------------------' for card in player1.battlefield]))
        elif len(player2.battlefield) >= len(player1.battlefield) and len(player2.battlefield)<=5:
            print(''.join(['--------------------------------' for card in player2.battlefield]))
        else:
            print(''.join(['--------------------------------' for card in range(5)]))
        for card in player1.battlefield:
            if card.card_type=="Creature":
                print((f" {card.name} {card.attack_strength}/{card.defense_strength} (Creature) "), end="\t",)
            else:
                print((f" {card.name} {card.resource_cost} ({card.card_type}) "), end="\t")
        print(f"\n\n{player1.name}'s Life Total: {player1.life_points}")
        print(f"Resources: { player1.gold} /8\n")
        print(f"Cards in hand of {player1.name}:")
        print('\n'.join([f"\t{card.name}" for card in player1.cards_in_hand]), end ="\n\n\n")
        print(''.join(['********************************' for card in range(5)]))