import os
import sys
import json
from datetime import datetime
from flask import request, jsonify, Flask, make_response

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


entries = []


@app.route('/api', methods=['GET', 'POST'])
def list_messages():

    if request.method == 'GET':
        s = "<html><head></head><body><ul>"
        for timestamp, ip, message in entries:
            print(timestamp, ip, message)
            s += "<li>" + str(timestamp) + "&nbsp;" + ip + \
                "&nbsp;" + message + "</li>"
        s += "</ul></body></html>"

        return s
    elif request.method == 'POST':
        try:
            cnetid = json.loads(request.data.decode("utf-8"))['cnetid']
            print("CnetID:", cnetid)
            entries.append((datetime.now(), request.remote_addr, cnetid))
            return make_response("Entry added.", 200)
        except:
            return make_response("Server error.", 500)
