from flask import Flask, jsonify

app = Flask(__name__)

user = {
    "username": "user1",
    "password": "password2"
}

user1 = {
    "username": "charles",
    "password": "definitelyNotPassword"
}

users = [user, user1]

@app.route('/login')
def initializeLogin():
    return jsonify(users)

if __name__ == '__main__':
    app.run()