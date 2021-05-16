from flask import Flask, request, abort
import time

db = []

app = Flask(__name__)

@app.route("/")
def run_flask():
    return "Server Run"

@app.route("/send", methods = ['POST'])
def send_messages():
    if not isinstance(request.json, dict):
        return abort(400)

    name = request.json.get('name')
    text = request.json.get('text')

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if name=='' or text=='':
        return abort(400)

    messages = {
        "name": name,
        "time": time.time(),
        "text": text
    }
    db.append(messages)
    return {'OK': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return {'messages': messages[:100]}


app.run()