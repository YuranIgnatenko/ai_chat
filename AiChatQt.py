import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

from flask import Flask, render_template, request
from ai import AgentAi

from threading import Thread

from datetime import datetime

app_flask = Flask(__name__)
agent = AgentAi()

class Message():
	def __init__(self, text):
		self.text = text
		self.date_label = datetime.now()

@app_flask.route('/')
def root():
	return render_template('chat.html')

@app_flask.route('/send', methods=['post'])
def send():
	text = request.get_data()
	text = str(text, encoding='utf-8')
	new_message = Message(agent.get_result(text)) 
	return new_message.text

def start_flask():
	app_flask.run(debug=True)

def start_qt():
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
	web_view.setUrl(Q_URL) # Замените данный URL на URL вашего Flask приложения

	window.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	# th_flask = Thread(target=start_flask)
	# th_flask.start()

	th_qt = Thread(target=start_qt)
	th_qt.start()
	
	start_flask()

