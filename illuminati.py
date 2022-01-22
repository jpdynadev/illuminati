from flask import Flask

app = Flask(__name__)

@app.route('/')
def initializeLogin():
    return 'Initalizing login'

if __name__ == '__main__':
    app.run()