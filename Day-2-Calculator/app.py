user_input_num_1 = input("Please enter your first number >> ")
user_input_num_2 = input("Please enter your second number >> ")
user_input_opertaion = input("Please choose your operation from this list [ +  -  /  * ] >> ")
user_inputs = {"num_1":user_input_num_1,"operation":user_input_opertaion,"num_2":user_input_num_2}

def calcualte():
   match user_inputs["operation"]:
       case "-" :
           return int(user_inputs["num_1"]) - int(user_inputs["num_2"])
       case "+" :
           return int(user_inputs["num_1"]) + int(user_inputs["num_2"])
       case "/" :
            if(not int(user_inputs["num_2"])):
                return "Division by zero. Danger zone !!"
            else:
                return int(user_inputs["num_1"]) / int(user_inputs["num_2"])
       case "*" :
           return int(user_inputs["num_1"]) * int(user_inputs["num_2"])
    
print(f"Result is: {calcualte()}")

