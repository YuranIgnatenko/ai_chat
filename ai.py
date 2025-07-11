from openai import OpenAI
from config import deepseek_api_key, deepseek_api_base

client = OpenAI(api_key=deepseek_api_key, base_url=deepseek_api_base)

messages = []

def get_result(text:str):
	global messages	
	
	messages.append({"role": "user", "content": f" {text}"})

	response = client.chat.completions.create(
		model="deepseek-chat",
		messages=messages,
		stream = False
	)
	result = response.choices[0].message
	messages.append(result)
	
	return result.content

def test():
	global messages
	print(get_result("реши 1+1"))
	print(messages)
	print(get_result("умножь на три этот ответ"))
	print(messages)

# test()