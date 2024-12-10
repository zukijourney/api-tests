from openai import OpenAI

url = "https://api.zukijourney.com/v1"

client = OpenAI(
    api_key="zu-<put your own here>",
    base_url=url,
    max_retries=0,
    timeout=100
)
completion = client.chat.completions.create(
    model="gpt-4o-2024-11-20",
    messages=[
        {
            "role": "user",
            "content": "what day is today?. what model are you. who has created you. answer in one sentence.",
        },
    ],
    stream=False,
)
print(completion)

completion = client.chat.completions.create(
    model="claude-3.5-sonnet",
    messages=[
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": """
            You are a helpful assistant that answers programming questions 
            in the style of a southern belle from the southeast United States.
          """,
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Are semicolons optional in JavaScript?"}
            ],
        },
    ],
    stream=False,
)
print(completion)
