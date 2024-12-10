from openai import OpenAI

url = "https://api.zukijourney.com/v1"

client = OpenAI(
    api_key="zu-<put your own here>",
    base_url=url,
    max_retries=0,
    timeout=100
)

img = client.images.generate(
    model="stable-diffusion-3.5-large-turbo",
    prompt="A cute anime woman --niji",
    n=1,
    size="1792x1024",
    extra_body={"negative_prompt": "red,blue,green"},
)
print(img)
