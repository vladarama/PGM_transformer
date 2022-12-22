from flask import Flask
from image_processing import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


print()
