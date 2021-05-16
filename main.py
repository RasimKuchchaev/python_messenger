import time

db = [
    {
        "text": "Hello 1",
        "time": time.time(),
        "name": "Nick"
    },
    {
        "text": "Hello 2",
        "time": time.time(),
        "name": "Jane"
    }
    ]


def print_mesages(qwe):
    for message in qwe:
        print(message["name"], message["time"])
        print(message["text"])
        print()
    # print(db)

def send_messages(name, text):
    messages = {
        "name": name,
        "time": time.time(),
        "text": text
    }
    db.append(messages)


def get_messages(after):
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return messages


send_messages("Rasim", "How are you ?")
print_mesages(db)
mesages = get_messages(0)
send_messages("Rasim1", "How are you 1?")
mesages = get_messages(mesages[-1]['time'])
print_mesages(mesages)
