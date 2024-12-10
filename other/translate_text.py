import requests, json

url = "http://api.zukijourney.com/v1/text/translations"
headers = {"Authorization": "Bearer zu-<put your own here>",'Content-Type': 'application/json'}
json_data = {
    "text": "[ 종말게임 하르마게돈에 오신 것을 환영합니다. ] ",
    "src": "ko",
    "target": "en",
    "model": "google-translate",
}
response = requests.post(url, data=json.dumps(json_data), headers=headers)
print(response.text)
