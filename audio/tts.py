from openai import OpenAI

client = OpenAI(
    base_url="https://api.zukijourney.com/v1",
    api_key="zu-<put your own here>",
)

response = client.audio.speech.create(
    model='bark', voice='alloy', input="The quick brown fox jumped over the lazy dog."
)
response.stream_to_file(f"test-audio.mp3")
