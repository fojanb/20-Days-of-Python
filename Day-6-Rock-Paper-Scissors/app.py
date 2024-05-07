from random import randint
options = ["Rock","Scissors","Paper"]
computer = options[randint(0,2)]
def get_user_input():
    return input("Rock, Paper, Scissors? :\n")
    
def compare_players_input():
    if(player == computer):
        print("Tie !")
    elif (player == "Rock"):
        if(computer == "Paper"):
            print("Computer:", computer, "You:", player)
            print("You lose!", computer, "covers", player)
        else:
            print("Computer:", computer, "You:", player)
            print("You win!", player, "breaks", computer)
    elif (player == "Paper"):
        if(computer == "Rock"):
            print("Computer:", computer, "You:", player)
            print("You Win!", player, "covers", computer)
        else:
            print("Computer:", computer, "You:", player)
            print("You lose!", computer, "cuts", player)
    elif (player == "Scissors"):
        if(computer == "Rock"):
            print("Computer:", computer, "You:", player)
            print("You lose!", computer, "breaks", player)
        else:
            print("Computer:", computer, "You:", player)
            print("You win!", player, "cuts", computer)
        
player = get_user_input()
compare_players_input()