from random import randint
from colors import BRIGHT_CYAN,BRIGHT_MAGENTA,BLUE,RED,GREEN,RESET

options = ["Rock","Scissors","Paper"]
def get_user_input():
    player_turn = input(BRIGHT_CYAN + " Enter 'r' for Rock\n Enter 'p' for Paper\n Enter 's' for Scissors\n >> " + RESET)
    match(player_turn.upper()):
        case 'R':
            return options[0]
        case 'S':
            return options[1]
        case 'P':
            return options[2]
        case _:
            print(RED + "Not a valid input !" + RESET)
            try_again = input("Would you like to try again? (y/n)\n")
            if(try_again.upper() == 'Y'):
                start()
            else:
                print(BRIGHT_MAGENTA + "Not a problem ! Have some rest." + RESET)
                exit(0);

def compare_players_input(player,computer):
    if(player == computer):
        print(BLUE + "Computer:"+ computer+" - "+"You:"+ player + RESET)
        print("Tie !")
    elif (player == "Rock"):
        if(computer == "Paper"):
            print(BLUE + "Computer:"+ computer+" - "+"You:"+ player + RESET)
            print(RED + "You lose... "+computer+ " covers "+ player + RESET)
        else:
            print(BLUE + "Computer:"+ computer+" - "+"You:"+ player + RESET)
            print(GREEN + "You win! "+player+ " breaks "+ computer+RESET)
    elif (player == "Paper"):
        if(computer == "Rock"):
            print(BLUE + "Computer:"+ computer+" - "+"You:"+ player + RESET)
            print(GREEN + "You Win! "+ player+ " covers "+ computer+RESET)
        else:
            print(BLUE + "Computer: "+ computer +" - "+"You: "+ player + RESET)
            print(RED + "You lose... "+ computer + " cuts "+ player+RESET)
    elif (player == "Scissors"):
        if(computer == "Rock"):
            print(BLUE + "Computer:"+ computer+" - "+"You:"+ player + RESET)
            print(RED+"You lose... "+ computer+ " breaks "+ player+RESET)
        else:
            print(BLUE + "Computer:"+ computer+" - "+"You:"+ player + RESET)
            print(GREEN + "You win! "+ player + " cuts "+ computer +RESET)
     
def continue_play():
    is_agree = input("Do you want to keep on playing ? (y/n)\n")
    if(is_agree.upper() == 'Y'):
       start()
    else:
        print("Ok, See you then and bye bye.")
        
def start():   
    computer = options[randint(0,2)] 
    player = get_user_input()
    compare_players_input(player,computer)
    continue_play()
    
start()