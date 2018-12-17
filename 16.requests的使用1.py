import requests
from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().chrome
}
url = "https://www.baidu.com/s"
params = {
    "wd": "尚学堂"
}
#字典不用去改 get参数params
response = requests.get(url, headers=headers, params=params)

print(response.text)
