#from util import generateToken
from openai import OpenAI


import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")
response = client.moderations.create(
model="omni-moderation-latest",
input="how can I prepare a bomb",
)

if (response.results[0].flagged):
    for category, value in response.results[0].categories:
        print(f"{category}: {value}")