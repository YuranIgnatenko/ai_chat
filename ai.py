from openai import OpenAI
from config import deepseek_api_key, deepseek_api_base

import sys

# client = OpenAI(api_key=deepseek_api_key, base_url=deepseek_api_base)

# messages = []

class AgentAi():
	def __init__(self):
		self.client = OpenAI(api_key=deepseek_api_key, base_url=deepseek_api_base)
		self.messages = []
		# self.test()

	def get_result(self, text:str) -> list:
		
		self.messages.append({"role": "user", "content": f" {text}"})

		response = self.client.chat.completions.create(
			model = "deepseek-chat",
			messages = self.messages,
			stream = False
		)
		result = response.choices[0].message
		self.messages.append(result)

		return result.content
		# return self.messages

	def test(self):
		print(self.get_result("реши 1+1")[0])
		print(self.get_result("умножь на три этот ответ")[0])

