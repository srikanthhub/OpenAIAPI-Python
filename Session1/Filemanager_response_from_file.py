from openai import OpenAI
client = OpenAI()

file = client.files.create(
    file=open("Srikanth_Resume.pdf", "rb"),
    purpose="user_data"
)

completion = client.chat.completions.create(
model="gpt-4o",
messages=[
    {
        "role": "user", 
        "content": [{
            "type": "file",
            "file : {"
            "file_id": file.id
        },
        {
            "type": "text",
            "content": "What is the main topic of this file?"
        },
    ]
    }    
]
)