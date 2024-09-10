from openai import OpenAI

client = OpenAI(
    base_url="https://api.zukijourney.com/v1",
    api_key="zu-<put your own here>",
)

model_list = client.models.list()
print(model_list)
