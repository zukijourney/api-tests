from openai import OpenAI

client = OpenAI(
    base_url="https://zukijourney.xyzbot.net/v1",
    api_key="zu-<put your own here>",
)

img = client.images.generate(
    model="sdxl-turbo", prompt="A cute baby sea otter", n=1, size="1024x1024"
)
print(img)
