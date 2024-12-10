from openai import OpenAI

url = "https://api.zukijourney.com/v1"

client = OpenAI(
    api_key="zu-<put your own here>",
    base_url=url,
    max_retries=0,
    timeout=100
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "respond like an uwu anime catgirl"},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://files.catbox.moe/mx7saf.png"},
                },
            ],
        },
    ],
    max_tokens=300,
)

print(response)