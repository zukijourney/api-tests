from openai import OpenAI

url = "http://api.zukijourney.com/v1"

client = OpenAI(
    api_key="zu-<put your own here>",
    base_url=url,
    max_retries=0,
    timeout=100,
)

models_provided = [
    ("tts-1", "alloy"),
    # ("tts-1-hd", "alloy"),
    # ("elevenlabs", "george"),
    # ("speechify", "mrbeast"),
]
for m in models_provided:
    response = client.audio.speech.create(
        model=m[0],
        voice=m[1],
        input="pierangelo can suck the rust off my ballsack",
    )
    print(f"Model: {m[0]} finished.")
    response.stream_to_file(f"{m[0]}-gchungu-audio.mp3")

