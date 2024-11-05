import requests
api_key="d032eaa77e3343a19c02aed248a8e4e0"
url="https://newsapi.org/v2/everything?q=tesla&from=2024-10-05&" \
    "sortBy=publishedAt&apiKey=d032eaa77e3343a19c02aed248a8e4e0"
request=requests.get(url)
content=request.json()
print(content['articles'])
for val in content["articles"]:
    print(val['author'],end=" : ")
    print(val['content'],end=" : ")
    print(val['description'],end=" : ")
