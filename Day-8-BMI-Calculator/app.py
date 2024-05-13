from math import pow
user_measures = {}
weight = ["weight","kg","BMI"]
height = ["height","cm","BMI"]
def welcome_message():
    print("\nWelcome to the BMI Calculator application.\n")
    
def get_metrics(metrics):
    value = int(input(f"Please enter your {metrics[0]} in {metrics[1]}:\n"))
    user_measures[metrics[0]] = value
    
def calculate_BMI():
    user_BMI_value = user_measures["weight"]/pow(user_measures["height"]/100,2)
    user_measures["BMI"] = truncate_float(user_BMI_value,2)
    
def truncate_float(float_number, decimal_places):
    multiplier = 10 ** decimal_places
    return int(float_number * multiplier) / multiplier

def results_BMI():
    if(user_measures["BMI"] < 18.5):
        print(f"\nYour BMI is {user_measures["BMI"]} - Underweight")

    elif(user_measures["BMI"] >= 18.5 and user_measures["BMI"] <= 24.9): 
        print(f"\nYour BMI is {user_measures["BMI"]} - Normal Weight")
        
    elif(user_measures["BMI"] >= 25.0 and user_measures["BMI"] <= 29.9):
        print(f"\nYour BMI is {user_measures["BMI"]} - Overweight")
              
    elif(user_measures["BMI"] >= 30.0 and user_measures["BMI"] <= 34.9):
        print(f"\nYour BMI is {user_measures["BMI"]} - Obesity Class 1")
        
    elif(user_measures["BMI"] >= 35.0 and user_measures["BMI"] <= 39.9):
        print(f"\nYour BMI is {user_measures["BMI"]} - Obesity Class 2")
        
    elif(user_measures["BMI"] >= 40):
        print(f"\nYour BMI is {user_measures["BMI"]} - Obesity Class 3")   
    else:
        print("Something went wrong...")
        
   
welcome_message()
get_metrics(weight)
get_metrics(height)
calculate_BMI()
results_BMI()


