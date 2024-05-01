
from colors import GREEN,RED,BRIGHT_MAGENTA,BRIGHT_YELLOW,BLUE,RESET
def get_user_inputs():
    print("===== Welcome to the Calculator App =====")
    user_input_opertaion = input(" Enter 'a' for addition\n Enter 's' for subtraction\n Enter 'm' for multiplicatio\n Enter 'd' for division\n >>")
    user_input_num_1 = input(GREEN + "Please enter your first number >> " + RESET)
    user_input_num_2 = input(BRIGHT_MAGENTA + "Please enter your second number >> " + RESET)
    user_inputs = {"num_1":user_input_num_1,"operation":user_input_opertaion,"num_2":user_input_num_2}
    print(BRIGHT_YELLOW + f"Ans = {claculator(user_inputs)}" + RESET)
    rerender_app()
    
def handle_error():
    try_again = input(RED + "Not a valid operation. Do you want to try again? (y/n)\n"+RESET)
    if(try_again == "y" or "Y"):
        get_user_inputs()
        
def claculator(data):
    if(data["operation"].isalpha()):
        match data["operation"]:
            case "s" :
                return int(data["num_1"]) - int(data["num_2"])
            case "a" :
                return int(data["num_1"]) + int(data["num_2"])
            case "d" :
                if(not int(data["num_2"])):
                    return "Division by zero. Danger zone !!"
                else:
                    return int(data["num_1"]) / int(data["num_2"])
            case "m" :
                return int(data["num_1"]) * int(data["num_2"])
            case _ :
                handle_error()
    else:
        handle_error()
       
def rerender_app():
    user_wants_to_rerender_app = input(BLUE + "Would you like to do more calculations? (y/n)\n" + RESET)
    if(user_wants_to_rerender_app == "y"):
        get_user_inputs()
    else:
        print("Thanks for using our app. See you later.")
        exit(0)
    
get_user_inputs()
