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
        temperature=1.5, #controls the randomness of the output. 0 is deterministic, 1 is random, 2 is very random.
        top_p=0.5, #controls the diversity of the output. 0 is deterministic, 1 is random, 2 is very random.
        frequency_penalty=0.0, #controls the repetition of the output. 0 is no penalty, 1 is high penalty.
        presence_penalty=0.0, #controls the presence of the output. 0 is no penalty, 1 is high penalty.
        response_format={"type": "text"}, #controls the format of the output. text is plain text, json is json, html is html.
        n=1, #controls the number of responses. 1 is one response, 2 is two responses, 3 is three responses.
        max_tokens=1000, #controls the length of the output. 0 is no limit, 1 is one token, 2 is two tokens.
        stop=None, #controls the stopping of the output. None is no stop, 1 is one stop, 2 is two stops.
        messages=message,
    )

    assistant_response = completion.choices[0].message.content
    print(f"Assistant: {assistant_response}\n")
    print('*' * 100)
    print('*'*20, completion.usage.prompt_tokens, '*'*20, completion.usage.completion_tokens, '*'*20, completion.usage.total_tokens, '*'*20)
    message.append({"role": "assistant", "content": assistant_response})    