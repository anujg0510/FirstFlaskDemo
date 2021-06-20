from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    return "<h1>Demo Flask Application</h1>"

if __name__ == "__main__":
    app.run()