# importing Flask and other modules
from flask import Flask,jsonify,request,render_template

from requests import get

# Setup a server:
app = Flask(__name__)

# ----------------------------------------------
#set route for /repositories 
@app.route('/repositories',methods =["GET"])
def get_data():
    username = request.args.get('username')
    resposne = get(f"https://api.github.com/users/{username}/repos")
    data = resposne.json()
    return jsonify(data)
# ----------------------------------------------

#set route for homepage 
@app.route('/')
def get_home(name=None):
    return render_template('index.html',name=name)
# ----------------------------------------------
# run the flask app
if __name__ == "__main__":
    app.run()