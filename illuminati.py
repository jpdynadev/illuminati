from flask import Flask, jsonify, request

app = Flask(__name__)

user = {
    "username": "user1",
    "password": "password2"
}

user1 = {
    "username": "charles",
    "password": "password1"
}

users = [user, user1]

@app.route('/login')
def initializeLogin():
    username = request.args.get('username')
    password = request.args.get('password')
    for user in users:
        if user["username"] == username:
            return jsonify(True) if user["password"] == password else jsonify(False)
    
if __name__ == '__main__':
    app.run()
