import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/', methods=['GET'])
def home():
    return "<h1>Rest API</h1><p>This site is under construction.</p>"

app.run()
