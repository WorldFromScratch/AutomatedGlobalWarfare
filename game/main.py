import os
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

DATABASE = {}
path = "D:\\Walkthrough\\GlobalWarfare\\"
filename = "db.txt"

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/enrollUser', methods=['POST'])
def enrollUser():
    print request.form

    if "users" not in DATABASE:
        DATABASE['users'] = {}

    DATABASE['users'][request.form['name']] = {"robots":{}}

    user = DATABASE['users'][request.form['name']]
    return jsonify({"status": 200, "user": user})


@app.route('/compileRobot', methods=['POST'])
def compileRobot():
    print request.form
    return jsonify({"status": 200})


@app.route('/startBattle', methods=['POST'])
def startBattle():
    print request.form
    return jsonify({"status": 200})


@app.route('/nextRound', methods=['GET'])
def nextRound():
    print request.form
    return jsonify({"status": 200})


@app.route('/getEnemies', methods=['GET'])
def getEnemies():
    print request.form
    return jsonify({"status": 200})


@app.route('/saveGame', methods=['GET'])
def saveGame():
    print request.form

    file = open(os.path.join(path, filename), "wb")
    file.write(str(DATABASE))
    file.close()

    return jsonify({"status": 200})



if __name__ == "__main__":
    file = open(os.path.join(path, filename), "rb")
    DATABASE = eval(file.read())
    file.close()

    app.run()