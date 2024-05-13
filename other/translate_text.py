import requests, json

headers = {"Authorization": "Bearer zu-<put your own here>"}
json_data = {
    "text": "[ 종말게임 하르마게돈에 오신 것을 환영합니다. ] ",
    "src": "ko",
    "target": "en",
}
url = "https://zukijourney.xyzbot.net/v1/text/translations"
response = requests.post(url, data=json.dumps(json_data), headers=headers)
print(response.text)
