from flask import Flask,jsonify,request,render_template
from requests import get

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    resposne = get(f"https://api.github.com/users/fojanb/repos")
    data = {"name": resposne.json()[0]["name"]}
    return jsonify(data)


@app.route('/')
def get_home(name=None):
    return render_template('index.html',name=name)

if __name__ == "__main__":
    app.run()