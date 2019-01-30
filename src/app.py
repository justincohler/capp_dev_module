import os
import sys
from flask import Flask

app = Flask(__name__)


@app.route('/directory')
def list_directory():
    PATH = "~"
    files = os.listdir(PATH)

    s = "<html><head></head><body><ul>"
    for file in files:
        s += "<li>" + file + "</li>"
    s += "</ul></body></html>"

    return s
