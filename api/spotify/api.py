import flask

from spotify import run
from flask_cors import CORS


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "hello"

@app.route('/order/<characteristic>')
def showOrder(characteristic):
    # show the user profile for that user
    return run(characteristic)


app.run()