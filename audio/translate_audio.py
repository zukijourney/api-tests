from openai import OpenAI

client = OpenAI(
    base_url="https://api.zukijourney.com/v1",
    api_key="zu-<put your own here>",
)

audio_file = open("test-audio.mp3", "rb")
transcript = client.audio.translations.create(model='whisper', file=audio_file)
print(transcript)

