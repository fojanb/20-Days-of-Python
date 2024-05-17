# importing Flask and other modules
from flask import Flask,jsonify,request,render_template,make_response

from requests import get

# Setup a server:
app = Flask(__name__)

# ----------------------------------------------
#set route for /repositories 
@app.route('/repositories',methods =["GET"])
def get_data():
    username = request.args.get('username')
    resposne = get(f"https://api.github.com/users/{username}/repos")
    data = jsonify(resposne.json())
    return render_template('repos.html',data=data)

# ----------------------------------------------
#set route for homepage 
@app.route('/')
def get_home():
    return render_template('index.html')
# ----------------------------------------------
# run the flask app
if __name__ == "__main__":
    app.run()
# Useful
# https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask