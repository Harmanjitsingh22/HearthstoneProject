# Name : HARMANJIT SINGH
# Student no. : 300212091
# UFV email  : harmanjit.singh2@student.ufv.ca

import random
from Turn import Turn
from Display import Display
from Player import Player

class GameEngine(Display, Player):
    def __init__(self):
        self.players = {} 

    
    # allows player to enter their name
    # def get_player_name(self, name):
    #     self.name = self.player.set_name(name)
        
    def no_of_times_to_draw_card(self, player_to_draw_card, initial_stage=False):

        if initial_stage:
            if player_to_draw_card.name !="Computer":
                while True:
                    draw_card_times =input("How many cards you want to drawn from deck: ")
                    try:
                        draw_card_times =int(draw_card_times)
                        if draw_card_times<=3 and draw_card_times>0:
                            break
                        elif draw_card_times<=0:
                            print("Negative value or 0 is not allowed. Enter valid number only.")
                        else:
                            print("Initially, You can only draw up to 3 card.")
                    except:
                        print("Please enter valid number only")
            else:
                # get a random number from 1 o 3 by using random.randint() function 
                # Source : https://www.w3schools.com/python/ref_random_randint.asp
                draw_card_times = random.randint(1,3)

            for _ in range(draw_card_times):   
                player_to_draw_card.player_draw_card()
        else:
            player_to_draw_card.player_draw_card()

    def execute_turn(self, player_turn, gold):
        turn = Turn(player_turn)
        turn.execute(self.player1 if player_turn==self.player2 else self.player2, gold)

    # check if the game is over
    def is_game_over(self, alive_player):
        # return True if game is over
        # game ends when one player's life_points <=0
        if  not alive_player.is_player_alive():  # if self.player1.is_player_alive <= 0: 
            return True
        elif alive_player.cards==[]:# if deck is empty
            return True
        else:
            return False
        

    # determine the winner
    def determine_winner(self):
        # a winner is determine if player 1's score is greater than player'2 score
        # ALTERNATIVE: a winner is determine if player 1's life_points is greater than player 2's life_points
        # BUT NOT TRUE 
        # when the game is over, the winner is the one who still has life_points
        # return None if game is not over (i.e. nobody has won yet)
        if self.is_game_over(self.player1) or self.is_game_over(self.player2):
            if self.player1.life_points>self.player2.life_points:
                print("Game Over!")
                print(f"{self.player1.name} Wins \U0001F3C6")
                return True
            else:
                print("Game Over!")
                print(f"{self.player2.name} Wins \U0001F3C6")
                return True
        else:
            print("Game is not over yet!")
            return False
        
    # Game loop
    def play_game(self):
        
        self.player1.gold = 1
        self.player2.gold=1
        while self.player1.life_points > 0 and self.player2.life_points > 0:
            self.print_battlefield(self.player1, self.player2)
            self.no_of_times_to_draw_card(self.player1)
            self.no_of_times_to_draw_card(self.player2)
            self.print_battlefield(self.player1, self.player2)
            self.execute_turn(self.player1, self.player1.gold)
            self.execute_turn(self.player2, self.player2.gold)
            self.player1.gold +=1
            self.player2.gold+=1
            if self.player1.gold >8:
                self.player1.gold =1
            elif self.player2.gold>8:
                self.player2.gold =1

        self.print_battlefield(self.player1, self.player2)

        self.determine_winner()

    # starting the game (setup)
    def setup_game(self):
        # Deck is already created in deck class. Therefore, no need to call again create_deck function.
        # self.deck.create_deck()
        current_player_index=0
        current_player = list(self.players.values())[current_player_index]
        self.no_of_times_to_draw_card(current_player, initial_stage = True)
        self.player1 =current_player
        current_player_index = (current_player_index + 1) % len(self.players)
        other_player = list(self.players.values())[current_player_index]
        self.no_of_times_to_draw_card(other_player, initial_stage =True)
        self.player2 =other_player
        self.play_game()
    