from openai import OpenAI

client = OpenAI(
    base_url="https://api.zukijourney.com/v1",
    api_key="zu-<put your own here>",
)

response = client.chat.completions.create(
    model="reka-flash",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Why is this image funny?"},
                {
                    "type": "image_url",
                    "image_url": "https://files.catbox.moe/e9p1z1.png", # or add a base64 string here of "data:image....base64,..." type
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])
