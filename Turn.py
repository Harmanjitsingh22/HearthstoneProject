import random
from Player import Player

class Turn(Player):

    def __init__(self, player):
        super().__init__(player)
        self.player = player

    def execute(self, opponent, gold):
        super().__init__(gold=gold)
        self.player.gold = gold
        if self.player.name !="Computer":
            play=True
            play_again = True
            while play==True:
                # Select a card to play
                while play_again==True:
                    card_index =1
                    for card in self.player.cards_in_hand:
                        print(f"\t{card_index}. {card.name} ({card.card_type}) - {card.resource_cost} resources")
                        card_index+=1

                    selected_card=input("Which card do you want to play : ")
                    try:
                        selected_card=int(selected_card)
                        selected_card=int(selected_card)-1
                        if  selected_card>=len(self.player.cards_in_hand) or selected_card<0 :
                            print("Please enter valid number")
                        else:
                            play_again=False
                    except:
                        print("please enter number only")
                card_cards_in_hand = self.player.cards_in_hand[selected_card]
                # if player drew a creature card
                if self.player.cards_in_hand[selected_card].card_type=="Creature":
                    # Creature card automatically attack the opponent'card
                    has_played = self.player.play_creature(self.player.cards_in_hand[selected_card])
                    if has_played ==False:
                        play_again=False
                    else:
                        for card in self.player.battlefield:
                            if card==card_cards_in_hand:
                                self.player.gold -= card.resource_cost

                # if player drew a resource card
                elif self.player.cards_in_hand[selected_card].card_type=="Resource":
                    self.player.gold = self.player.play_resource(self.player.cards_in_hand[selected_card])

                # if player drew a spell
                elif self.player.cards_in_hand[selected_card].card_type=="Spell":
                    has_played = self.player.play_spell(self.player.cards_in_hand[selected_card], opponent)
                    if has_played ==False:
                        play_again=False
                    else:
                            for card in self.player.battlefield:
                                if card==card_cards_in_hand:
                                    self.player.gold -= card.resource_cost
                elif self.player.cards_in_hand[selected_card].card_type=="Equipment":
                    has_played = self.player.play_equipment(self.player.cards_in_hand[selected_card])
                    if has_played ==False:
                        play_again=False
                    else:
                            for card in self.player.battlefield:
                                if card==card_cards_in_hand:
                                    self.player.gold -= card.resource_cost
                ask_to_select_card_again = input("Do you want to play again (Y/N) :")
                if ask_to_select_card_again.upper() =="Y":
                    play_again=True
                else:
                    play=False


        else: # for computer
            computer_play_again = ["Y","N"]
            play_again = random.choice(computer_play_again)
            play = True
            while play==True:
            # Select a card to play
                while play_again=="Y":
                    if self.player.cards_in_hand!=[]:
                        random.shuffle(self.player.cards_in_hand)
                        selected_card = random.choice(self.player.cards_in_hand)
                        # select random card by computer
                        if opponent.cards_in_hand!=[]:
                            random.shuffle(opponent.cards_in_hand)
                            if selected_card.card_type=="Creature":
                                has_played = self.player.play_creature(selected_card)
                                if has_played ==False:
                                        play_again="N"
                                else:
                                    self.player.gold -= selected_card.resource_cost
                            elif selected_card.card_type=="Resource":
                                self.player.gold = self.player.play_resource(selected_card)

                            elif selected_card.card_type=="Spell":   
                                has_played = self.player.play_spell(selected_card, opponent)
                                if has_played ==False:
                                        play_again="N"
                                else:
                                    self.player.gold -= selected_card.resource_cost
                            elif selected_card.card_type=="Equipment":   
                                has_played = self.player.play_equipment(selected_card)
                                if has_played ==False:
                                        play_again="N"
                                else:
                                    self.player.gold -= selected_card.resource_cost
                        else:
                            opponent.attack_opponent_have_no_card(selected_card)

                    play_again="N"
                
                ask_to_select_card_again = random.choice(computer_play_again)
                ask_to_select_card_again = ask_to_select_card_again.upper()
                if ask_to_select_card_again =="Y":
                    play_again="Y"
                else:
                    play=False
                    
        self.player.attack_opponent(opponent)
        self.player.end_turn()
    