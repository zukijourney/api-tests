from openai import OpenAI

client = OpenAI(
    base_url="https://zukijourney.xyzbot.net/v1",
    api_key="zu-<put your own here>",
)
audio_file = open("test-audio.mp3", "rb")
transcript = client.audio.transcriptions.create(model='whisper', file=audio_file)
print(transcript)
