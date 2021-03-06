# qt.io
# https://build-system.fman.io/qt-designer-download
# https://www.riverbankcomputing.com/software/pyqt/download

# pip install PyQt6
# pyuic6 messenger.ui -o clientui.py
from datetime import datetime
import requests
from PyQt6 import QtWidgets, QtCore
import clientui


class Messenger(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self, server_host):
        super().__init__()
        self.setupUi(self)

        self.server_host = server_host

        # to run on button click:
        self.pushButton.pressed.connect(self.send_message)

        self.after = 0

        # to run by timer:
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def get_messages(self):
        try:
            response = requests.get(f'{self.server_host}/messages',
                                params={'after': self.after}
                                )
        except:
            return

        messages = response.json()['messages']
        for message in messages:
            message_time = datetime.fromtimestamp(message["time"])
            message_time = message_time.strftime('%d/%m/%Y %H:%M:%S')
            self.textBrowser.append(message["name"] + " " + message_time)
            self.textBrowser.append(message["text"])
            self.textBrowser.append('')

            self.after = message['time']

    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()
        try:
            response = requests.post(f'{self.server_host}/send',
                      json={'name': name, 'text': text}
                      )
        except:
            self.textBrowser.append('Server is not available')
            self.textBrowser.append('')
            return

        if response.status_code != 200:
            self.textBrowser.append('Enter name and text')
            self.textBrowser.append('')
            return

        self.textEdit.setText("")


app = QtWidgets.QApplication([])
windows = Messenger(server_host='http://127.0.0.1:5000')
windows.show()
app.exec()
