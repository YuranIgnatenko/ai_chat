from openai import OpenAI
from config import deepseek_api_key, deepseek_api_base

client = OpenAI(api_key=deepseek_api_key, base_url=deepseek_api_base)


def get_result(text:str):
	response = client.chat.completions.create(
		model="deepseek-chat",
		messages=[
			{"role": "system", "content": "Ассистент - чатбот ИИ"},
			{"role": "user", "content": f"{text}"},
		],
		stream = False
	)

	return response.choices[0].message.content
