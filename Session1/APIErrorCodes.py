#from util import generateToken
from openai import OpenAI, APIError, APIConnectionError, RateLimitError
import os
from dotenv import load_dotenv
load_dotenv()

try:
    messages = [
    {
    "role": "user",
    "content": "What is OpenAI"
    }
    ]
    client = OpenAI()
    response = client.chat.completions.create(
    messages=messages,
    model="gpt-4o-mini"
    )
except APIError as e:
    # Handle API error here, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")
    pass
except APIConnectionError as e:
    # Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")
    pass
except RateLimitError as e:
    # Handle rate limit error (we recommend using exponential backoff)
    print(f"OpenAI API request exceeded rate limit: {e}")
    pass
