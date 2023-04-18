from flask import Flask

app = Flask(__name__)


@app.route('/<city>')
def index(city: str):
    return f'Hello {city}'
