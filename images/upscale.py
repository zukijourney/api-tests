import requests

url = "https://api.zukijourney.com/v1/images/upscale"
headers = {"Authorization": "Bearer zu-<put your own here>"}

response = requests.post(url, headers=headers, files={"file": open("gaysex.png", "rb")})
print(response.status_code)
with open("gaysex_upscaled.png", "wb") as result_file:
    result_file.write(response.content)
