import random , string
all_characters = string.ascii_letters + string.digits + string.punctuation
length_of_password = int(input("Please enter the length of password:\n"))
password = ''.join(random.choices(all_characters,k=length_of_password))
print(password)
# https://www.makeuseof.com/tag/python-javascript-communicate-json/
# Flask, Django, FastAPI, Tornado, and many others come in handy for writing REST APIs in Python.