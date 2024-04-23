# Name : HARMANJIT SINGH
# Student no. : 300212091
# UFV email  : harmanjit.singh2@student.ufv.ca


from GameEngine import GameEngine
from Player import Player


def main():
    game = GameEngine()
    print("*******Player Vs Computer *******")
    while True:
        name = input(f"Enter player name without space: ")
        
        # Check if the name contains only alphabetic characters  
        # Source : https://www.w3schools.com/python/ref_string_isalpha.asp
        if  name.isalpha():
            if name=="Computer":
                print("Computer name is not allowed. Please enter other name.")
            else:
                game.players[name] = Player(name)
                #self.name = self.player2.set_name("Computer")
                break
        else:
            print("Invalid name! Please enter only alphabetic characters.")

    game.players["Computer"] = Player("Computer")
    
    game.setup_game()


if __name__ == "__main__":
    main()

