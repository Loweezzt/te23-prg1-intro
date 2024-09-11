   
from random import randint
player_one_roll = randint(1, 6)
player_two_roll = randint(1, 6)


play_game = ""
player_one_score = 0
player_two_score = 0
while play_game.upper() == "":

    print(f"Player one rolls {player_one_roll}!")
    print(f"Player two rolls {player_two_roll}!")

    if player_one_roll > player_two_roll:
        print(f"PLaya one wins easily with: {player_one_roll}.")
        player_one_score = 0 + 1
    elif player_two_roll > player_one_roll:
        print(f"Playa two wins easily with: {player_two_roll}.")
        player_two_score = 0 + 1
    else:
        print(
            f"No one wins, lets try again. They got that duece {player_one_roll}s")
        
    play_game = input("U wanna try again? Press enter")
