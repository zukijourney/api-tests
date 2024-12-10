import requests

url = "http://api.zukijourney.com/v1/images/upscale"
headers = {"Authorization": "Bearer zu-<put your own here>"}

response = requests.post(url, headers=headers, files={"file": ("gaysex.png", open("gaysex.png", "rb")), 'model':(None, 'upscale')})
print(response.status_code)
with open("gaysex_upscaled.png", "wb") as result_file:
    result_file.write(response.content)