from openai import OpenAI

url = "https://api.zukijourney.com/v1"

client = OpenAI(
    api_key="zu-<put your own here>",
    base_url=url,
    max_retries=0,
    timeout=100
)

embs = client.embeddings.create(
    model="text-embedding-3-small",
    input=["The food was delicious and the waiter..."],
    encoding_format="float",
)
print(embs)

