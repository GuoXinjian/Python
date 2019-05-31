import requests

url='http://127.0.0.1:5000'
res=requests.post(url)
print(res.content)