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
	app.run(host="127.0.0.1", port="5000")