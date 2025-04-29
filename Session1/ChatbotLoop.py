from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

message = [
    {"role": "system", "content": "You are an expert in AI and ML Subject. You can answer any question about AI and ML at an entry level learners. You must regret to answer questions not related to AI and ML"}
]


while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    message.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=message,
    )

    assistant_response = completion.choices[0].message.content
    print(f"Assistant: {assistant_response}\n")
    print('*' * 100)
    print('*'*20, completion.usage.prompt_tokens, '*'*20, completion.usage.completion_tokens, '*'*20, completion.usage.total_tokens, '*'*20)
    message.append({"role": "assistant", "content": assistant_response})    