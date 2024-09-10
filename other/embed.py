from openai import OpenAI

client = OpenAI(
    base_url="https://api.zukijourney.com/v1",
    api_key="zu-<put your own here>",
)

embs = client.embeddings.create(
    model="mxbai-embed-large-v1",
    input="The food was delicious and the waiter...",
    encoding_format="float",
)
print(embs)
