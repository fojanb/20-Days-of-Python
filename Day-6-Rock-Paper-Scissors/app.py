from random import randint
options = ["Rock","Scissors","Paper"]
computer = options[randint(0,2)]
def get_user_input():
    player_turn = input(" Enter 'r' for Rock\n Enter 'p' for Paper\n Enter 's' for Scissors\n >> ")
    match(player_turn.upper()):
        case 'R':
            return options[0]
        case 'S':
            return options[1]
        case 'P':
            return options[2]
        case _:
            print("Not a valid input !")
            exit(0);

def compare_players_input(player):
    if(player == computer):
        print("Tie !")
    elif (player == "Rock"):
        if(computer == "Paper"):
            print("Computer:", computer," - ","You:", player)
            print("You lose!", computer, "covers", player)
        else:
            print("Computer:", computer," - ", "You:", player)
            print("You win!", player, "breaks", computer)
    elif (player == "Paper"):
        if(computer == "Rock"):
            print("Computer:", computer," - ", "You:", player)
            print("You Win!", player, "covers", computer)
        else:
            print("Computer:", computer," - ", "You:", player)
            print("You lose!", computer, "cuts", player)
    elif (player == "Scissors"):
        if(computer == "Rock"):
            print("Computer:", computer," - ", "You:", player)
            print("You lose!", computer, "breaks", player)
        else:
            print("Computer:", computer," - ", "You:", player)
            print("You win!", player, "cuts", computer)
     
def continue_play():
    is_agree = input("Do you want to keep on playing ? (y/n)\n")
    if(is_agree.upper() == 'Y'):
       start()
    else:
        print("Ok, See you then and bye bye.")
        
def start():    
    player = get_user_input()
    compare_players_input(player)
    continue_play()
    
start()