import requests


res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=0110947")
js = res.json()
# print(js["results"][0]["prefcode"])
print(len(js["results"]))
# print(res.json())
