from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    n=2,
    messages=[
        {"role": "developer", "content": "Talk like a AI assistent."},
        {
            "role": "system",
            "content": "What is the future of software developers on this agentic AI generation?",
        },
    ],
)

print(completion.choices[0].message.content)
print('\n')
print('*' * 50)
print(completion.choices[1].message.content)