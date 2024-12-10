from openai import OpenAI

url = "http://api.zukijourney.com/v1"

client = OpenAI(
    api_key="zu-<put your own here>",
    base_url=url,
    max_retries=0,
    timeout=100,
)

audio_file = open("test-audio.mp3", "rb")
transcript = client.audio.transcriptions.create(model='whisper-1', file=audio_file)
print(transcript)
