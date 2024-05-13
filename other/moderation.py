from openai import OpenAI

client = OpenAI(
    base_url="https://zukijourney.xyzbot.net/v1",
    api_key="zu-<put your own here>",
)

moderation = client.moderations.create(input="I want to kill them.")
print(moderation)
