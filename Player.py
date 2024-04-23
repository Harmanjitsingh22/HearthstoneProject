# Name : HARMANJIT SINGH
# Student no. : 300212091
# UFV email  : harmanjit
# harmanjit.singh2@student.ufv.ca
from Deck import Deck
import random


class Player(Deck):
    def __init__(self , name="Computer", gold="1"):  # default starting life total
        self.life_points = 20
        self.name = name
        self.battlefield = []
        self.cards_in_hand = []
        self.resource=[]
        super().__init__()  
        self.create_deck()  # create a deck 
        self.dicard_pile =[]
        self.gold = gold

    def set_name(self, username):
        self.name = username

    def player_draw_card(self):
        if self.cards:
            card = self.draw_card_from_deck(self.name)  # Draw a card from the (class)
            if card:
                self.cards_in_hand.append(card)
            else:
                None

                
    def play_resource(self, selected_card):
        if selected_card.card_type == "Resource":
            self.resource.append(selected_card)
            self.cards_in_hand.remove(selected_card)
            print(f"{self.name} played a {selected_card.name} resource card.")
            gold = self.gold+selected_card.value
            return gold

    def play_creature(self, selected_card ):
        if selected_card.card_type == "Creature" and selected_card.resource_cost<= self.gold:            #TODO defend card select
            self.battlefield.append(selected_card)
            self.cards_in_hand.remove(selected_card)
            print(f"{self.name} played a {selected_card.name} {selected_card.attack_strength}/{selected_card.defense_strength} ({selected_card.card_type}) card.")
            return True
        else: # no enough resources to cast card
            print(f"sorry, {self.name} do not have a enough resources to cast {selected_card. card_type} card.")
            return False

    
    def attack_opponent(self, opponent):
        
        # Attack the opponent
        self.used_card_in_turn = self.battlefield

        #  First check if there is any creature card in battlefield
        ask_to_attack_more=True
        while ask_to_attack_more==True:
            if self.name !="Computer":
                attack_more = input("Do you want to attack the opponent (Y/N) :")
                attack_more=attack_more.upper()

                if attack_more!="Y":
                    ask_to_attack_more=False

                while attack_more=="Y":
                    card_idx=1
                    creature_card=False
                    for card in self.used_card_in_turn:
                        if card.card_type=="Creature":
                            print(f"\t{card_idx}.{card.name} {card.attack_strength}/{card.defense_strength} ({card.card_type})")
                            card_idx+=1
                            creature_card=True
                    
                    if creature_card==False:
                        print("All creature cards are used in this turn")
                        print("Now, You can try to attack in next turn")
                        creature_card=False
                        ask_to_attack_more=False
                            
                    creature_card_in_battlefield = False
                    for card in self.battlefield:
                        if card.card_type =="Creature":
                            creature_card_in_battlefield = True

                    if creature_card_in_battlefield==False: # if player has another card except creature
                        print("You do not have a creature card to attack.")
                        print("First play the creature card, then use it in next turn to attack the opponent")
                        creature_card=False
                        ask_to_attack_more=False

                
                    while creature_card ==True:
                        select_card_to_attack = input("which card do you want to use to attack enemy.")
                        try:
                            select_card_to_attack=int(select_card_to_attack)
                            select_card_to_attack=int(select_card_to_attack)-1
                            if  select_card_to_attack>=len(self.battlefield) or select_card_to_attack<0 :
                                print("Please enter valid number")
                            else:
                                # select a which opponent's creature card to destroy
                                if opponent.battlefield !=[]:
                                        opponent_card_index =1
                                        for oppo_card in opponent.battlefield:
                                            if oppo_card.card_type=="Creature":
                                                print("\n\n")
                                                print(f"\t{opponent_card_index}.{oppo_card.name} {oppo_card.attack_strength}/{oppo_card.defense_strength}({oppo_card.card_type}) card")
                                                opponent_card_index+=1
                                                while True:
                                                    attacked_card_index=input(f"At which {opponent.name}'s card, do you want to attack: ")
                                                    try:
                                                        attacked_card_index==int(attacked_card_index)
                                                        attacked_card_index=int(attacked_card_index)-1
                                                        if  attacked_card_index>=len(opponent.cards_in_hand) or attacked_card_index<0 :
                                                                print("Please enter valid number")
                                                        else:
                                                            attacked_card = opponent.cards_in_hand[attacked_card_index]
                                                            self.attack_opponent_with_card(self.used_card_in_turn[select_card_to_attack], opponent, attacked_card)
                                                            self.used_card_in_turn = self.used_card_in_turn.remove(self.used_card_in_turn[select_card_to_attack])
                                                    except:
                                                        print("please enter number only")
                                            else:
                                                # creature card directy attack opponent because opponent does not have a creature card to defend
                                                opponent.attack_opponent_have_no_creature( self.used_card_in_turn[select_card_to_attack])
                                                self.used_card_in_turn= self.used_card_in_turn.remove(self.used_card_in_turn[select_card_to_attack])
                                else:
                                    # creature card directy attack opponent because opponent does not have any card in battlefield
                                    opponent.attack_opponent_have_no_card( self.used_card_in_turn[select_card_to_attack])
                                    self.used_card_in_turn= self.used_card_in_turn.remove(self.used_card_in_turn[select_card_to_attack])
                        except:
                            print("please enter number only")

                        break
                    break
                

            else:  # for computer
                if self.battlefield !=[]:
                    while True:
                        select_card_to_attack= random.choice(self.used_card_in_turn)
                        if select_card_to_attack.card_type =="Creature" :
                            if opponent.battlefield !=[]:
                                while True:
                                    attacked_card = random.choice(opponent.battlefield)
                                    if attacked_card.card_type=="Creature":
                                        self.used_card_in_turn.remove(select_card_to_attack)
                                        self.attack_opponent_with_card(select_card_to_attack, opponent, attacked_card)
                                    else:
                                        # creature card directy attack opponent because opponent does not have a creature card to defend
                                        self.used_card_in_turn.remove(select_card_to_attack)
                                        opponent.attack_opponent_have_no_creature( select_card_to_attack)
                                        ask_to_attack_more=False
                                    break
                            else:
                                # creature card directy attack opponent because opponent does not have any card in battlefield
                                self.used_card_in_turn.remove(select_card_to_attack)
                                opponent.attack_opponent_have_no_card(select_card_to_attack)
                                ask_to_attack_more=False
                        break
                    ask_to_attack_more=False
                        

                
    def attack_opponent_with_card(self, selected_card, opponent, attacked_card):
        if selected_card.card_type == "Creature":
            print(f"{self.name}'s {selected_card.name} {selected_card.card_type} card attacks {attacked_card.name}.")
            loss_life = selected_card.attack_strength
            if attacked_card.card_type == "Creature":
                if selected_card.attack_strength > attacked_card.defense_strength:
                    self.used_card_in_turn.remove(selected_card)  # so thay player can not able to play one card again in one turn
                    print(f"{opponent.name}'s {attacked_card.name} {attacked_card.card_type} card defence the {self.name}'s {selected_card.name} {selected_card.card_type} card.")
                    print(f"{attacked_card.name} ({selected_card.card_type}) is destroyed by {selected_card.name} ({selected_card.card_type})")
                    opponent.dicard_pile.append(attacked_card)
                    loss_life = selected_card.attack_strength - attacked_card.defense_strength
                    print(f"{opponent.name} loss {loss_life} life-pionts.")
                    opponent.lose_life(loss_life)
                elif selected_card.attack_strength == attacked_card.defense_strength:
                    self.battlefield.remove(selected_card)
                    self.dicard_pile.append(selected_card)
                    opponent.battlefield.remove(attacked_card)
                    opponent.dicard_pile.append(attacked_card)
                    print(f"{opponent.name}'s {attacked_card.name} {attacked_card.card_type} card defence the {self.name}'s {selected_card.name} {selected_card.card_type} card.")
                    print(f" Both {self.name}'s {selected_card.name} ({selected_card.card_type}) and {opponent.name}'s {attacked_card.name} ({selected_card.card_type}) is destroyed by each other.")
                    # no life loss because both cards have same strength and defense power. 
                else:
                    print(f"{opponent.name}'s {attacked_card.name} {attacked_card.card_type} card defence the {self.name}'s {selected_card.name} {selected_card.card_type} card.")
                    attacked_card.defense_strength-= selected_card.attack_strength
                    # no life lose because defense is strong


    def attack_opponent_have_no_creature(opponent, card):
        # creature card directy attack opponent because opponent does not have a creature card to defend
        print(f"{opponent.name} does not have any creature card to defend.")
        print(f"Therefore, {card.name} {card.attack_strength}/{card.defense_strength} ({card.card_type}) card attacks the {opponent.name} directly.")
        print(f"{opponent.name} loss {card.attack_strength} life-pionts.")
        opponent.lose_life(card.attack_strength)

    def attack_opponent_have_no_card(opponent, card):
        # creature card directy attack opponent because opponent does not have any card in battlefield
        print(f"{opponent.name} does not have any card in battlefield.")
        print(f"Therefore, {card.name} {card.attack_strength}/{card.defense_strength} ({card.card_type}) card attacks the {opponent.name} directly.")
        print(f"{opponent.name} loss {card.attack_strength} life-pionts.")
        opponent.lose_life(card.attack_strength)

    def play_spell(self, selected_card, opponent):
        if selected_card.name=="Heal" and selected_card.resource_cost<=self.gold:
            gain_life_points =2
            print(f"{self.name} played a {selected_card.name} Spell.")
            print(f"{self.name} gain {gain_life_points} life-pionts.")
            self.gain_life(gain_life_points)
            self.cards_in_hand.remove(selected_card)
            self.dicard_pile.append(selected_card)
            return True

        elif selected_card.name=="Fireball" and selected_card.resource_cost<=self.gold:
            loss_life_point=2
            print(f"{self.name} played a {selected_card.name} Spell.")
            print(f"{opponent.name} loss {loss_life_point} life-pionts.")
            opponent.lose_life(loss_life_point)
            self.cards_in_hand.remove(selected_card)
            self.dicard_pile.append(selected_card)
            return True

        elif selected_card.name=="Destroy creature" and selected_card.resource_cost<=self.gold:
            destroy_card = opponent.choose_creature_card(selected_card)
            opponent.battelfield.remove(destroy_card)
            opponent.dicard_pile.append(destroy_card)
            print(f"{self.name} played a {selected_card.name} Spell.")
            print(f"{self.name}' {destroy_card.name} card has been destroyed by {self.name}.")
            self.cards_in_hand.remove(selected_card)
            self.dicard_pile.append(selected_card)
            return True
            return True
        elif selected_card.name=="Destroy creature" and selected_card.resource_cost<=self.gold:
            destroy_card = self.choose_creature_card(selected_card)
            opponent.battelfield.remove(destroy_card)
            opponent.dicard_pile.append(destroy_card)
            print(f"{self.name} played a {selected_card.name} Spell.")
            print(f"{self.name}' {destroy_card.name} card has been destroyed by {self.name}.")
            self.cards_in_hand.remove(selected_card)
            self.dicard_pile.append(selected_card)
            return True
    
        else: # no enough resources to cast card
            print(f"sorry, {self.name} do not have a enough resources to cast {selected_card. card_type} card.")
            return False
        
    def play_equipment(self, selected_card):
        if selected_card.name=="Sword" and selected_card.resource_cost<=self.gold:
            selected_card_for_equipment = self.choose_creature_card(selected_card)
            selected_card_for_equipment.attack_strength+=selected_card.resource_cost
            self.cards_in_hand.remove(selected_card)
            self.dicard_pile.append(selected_card)
            print(f"{selected_card.name} {selected_card.card_type} card applied to {selected_card_for_equipment} card.")
            for card in self.creatures:
                if card.name == selected_card_for_equipment.name:
                    print(f"\t {card.attack_strength}/{card.defense_strength} {card.name} ({card.card_type}) ")
            return True

        elif selected_card.name=="Shield" and selected_card.resource_cost<=self.gold:
            selected_card_for_equipment= self.choose_creature_card(selected_card)
            selected_card_for_equipment.defense_strength+=selected_card.resource_cost
            self.cards_in_hand.remove(selected_card)
            self.dicard_pile.append(selected_card)
            print(f"{selected_card.name} {selected_card.card_type} card applied to {selected_card_for_equipment} card.")
            for card in self.creatures:
                if card.name == selected_card_for_equipment.name:
                    print(f"\t {card.attack_strength}/{card.defense_strength} {card.name} ({card.card_type}) ")
            return True

        else: # no enough resources to cast card
            print(f"sorry, {self.name} do not have a enough resources to cast {selected_card. card_type} card.")
            return False

    def choose_creature_card(self, selected_card):
        play_again = True
        while play_again == True:
            # Select a card to play
            card_index =1
            creature=False
            self.creatures=[]
            for card in self.cards_in_hand:
                if card.card_type == "Creature":
                    print(f"\t{card_index}. {card.name} ({card.card_type}) - {card.resource_cost} resources")
                    card_index+=1
                    self.creatures.append(card)
                    creature=True

            if creature==False:
                print(f"{self.name} do not have any creature card to apply {selected_card.name} {selected_card.card_type} card.")
                break

            selected_card_for_equipment=input(f"At which card, do you want to apply {selected_card.name} {selected_card.card_type} card: ")
            try:
                selected_card_for_equipment=int(selected_card_for_equipment)
                selected_card_for_equipment=int(selected_card_for_equipment)-1
                if  selected_card_for_equipment>=len(self.creatures) or selected_card_for_equipment<0 :
                    print("Please enter valid number")
                else:
                    play_again = False
            except:
                print("please enter number only")

        return self.creatures[selected_card_for_equipment]
                    
    def add_card(self, card):
        self.cards.append(card)

    def end_turn(self):
        print(f"{self.name}'s turn ended.\n")

    def lose_life(self, loselife):
        self.loselife = loselife
        self.life_points -= self.loselife

    def gain_life(self, gainlife):
        self.gainlife = gainlife
        self.life_points += self.gainlife

    def is_player_alive(self):
        # 0 or less life_points means player is dead
        if self.life_points <= 0:
            return False
        else:
            return True