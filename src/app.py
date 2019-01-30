import os
import sys
from flask import Flask

app = Flask(__name__)


@app.route('/touch')
def list_sshd_directory():
    PATH = "~/capp_ssh"
    files = os.listdir(PATH)

    s = "<html><head></head><body><ul>"
    for file in files:
        s += "<li>" + file + "</li>"
    s += "</ul></body></html>"

    return s


@app.route('/scp')
def list_scpd_directory():
    PATH = "~/capp_scp"
    files = os.listdir(PATH)

    s = "<html><head></head><body><ul>"
    for file in files:
        s += "<li>" + file + "</li>"
    s += "</ul></body></html>"

    return s
