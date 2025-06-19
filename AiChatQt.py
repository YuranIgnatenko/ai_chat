import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

from flask import Flask, render_template, request
from ai import get_result

from datetime import datetime

app = Flask(__name__)

class Message():
	def __init__(self, text):
		self.text = text
		self.date_label = datetime.now()

pool_messages = []

@app.route('/')
def root():
	return render_template('chat.html')

@app.route('/send', methods=['post'])
def send():
	text = request.get_data()
	text = str(text, encoding='utf-8')
	new_message = Message(get_result(text))
	pool_messages.append(new_message)
	return pool_messages[-1].text


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	layout = QVBoxLayout()
	web_view = QWebEngineView()

	window.setWindowTitle('AiChatQt')
	window.resize(800, 600)

	layout.addWidget(web_view)
	window.setLayout(layout)
	url = 'http://127.0.0.1:5000'
	Q_URL = QUrl()
	Q_URL.setUrl(url)
	web_view.setUrl(Q_URL)

	window.show()

	sys.exit(app.exec_())