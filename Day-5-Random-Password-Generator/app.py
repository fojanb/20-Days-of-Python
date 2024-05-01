import random , string
from colors import BRIGHT_CYAN,BRIGHT_MAGENTA,RED,RESET

all_characters = string.ascii_letters + string.digits + string.punctuation
length_of_password = int(input(BRIGHT_MAGENTA + "Please enter the length of password:\n" + RESET))
password = ''.join(random.choices(all_characters,k=length_of_password))
print(BRIGHT_CYAN + "Your password is " + RED + f"{password}" + RESET)

# https://www.makeuseof.com/tag/python-javascript-communicate-json/
# Flask, Django, FastAPI, Tornado, and many others come in handy for writing REST APIs in Python.