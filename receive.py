import time
from datetime import datetime
import requests

after = 0

while True:
    response = requests.get('http://127.0.0.1:5000/messages',
                            params={'after': after}
                            )
    messages = response.json()['messages']
    for message in messages:
        message_time = datetime.fromtimestamp(message["time"])
        message_time = message_time.strftime('%d/%m/%Y %H:%M:%S')
        print(message["name"], message_time)
        print(message["text"])
        print()

        after = message['time']

    time.sleep(1)