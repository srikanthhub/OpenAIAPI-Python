import base64
from openai import OpenAI
client = OpenAI()

filename = input("Enter filename: ")

with open(filename, "rb") as f:
    data = f.read()

base64_string = base64.b64encode(data).decode("utf-8")

completion = client.chat.completions.create(
model="gpt-4o",
messages=[
    {
        "role": "user",
        "content": [
            {
                "type": "file",
                "file": {
                    "filename": filename,
                    "file_data": f"data:application/pdf;base64,{base64_string}",
                }   

            },
            {
                "type": "text",
                "text": "Compare all models of OpenAI"
            }
        ]
    }
]
)

print(completion.choices[0].message.content)
