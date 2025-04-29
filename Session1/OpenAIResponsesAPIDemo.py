from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

responses = client.responses.create(
    model="gpt-4o",
    input="What is Open AI and mention characteristics?")


print(responses)