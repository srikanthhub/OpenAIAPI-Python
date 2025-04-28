import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()


url = os.getenv("OPENAI_BASE_URL")+'chat/completions'
api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    }

data = {
    "model": "gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": "What is Open AI and mention characteristics?"
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
response_content = response.json()

print(response_content)
print(response_content['choices'][0]['message']['content'])