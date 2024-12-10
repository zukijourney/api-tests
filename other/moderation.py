from openai import OpenAI

url = "https://api.zukijourney.com/v1"

client = OpenAI(
    api_key="zu-<put your own here>",
    base_url=url,
    max_retries=0,
    timeout=100
)

moderation = client.moderations.create(input="I want to kill them.",model="omni-moderation-latest")
print(moderation)
