# from util import generateToken
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
messages = [
{
    "role": "user",
    "content": "What is OpenAI",
}]

# Make your OpenAI API request here
response = client.chat.completions.with_raw_response.create(
    messages=messages,
    model="gpt-4o-mini"
)

print(response.headers.get('x-ratelimit-limit-tokens'))
# get the object that `chat.completions.create()` would have returned
completion = response.parse()
print(completion.choices[0].message.content) 
