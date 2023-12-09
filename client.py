import requests


# url = 'https://c8e7-102-89-34-44.ngrok-free.app/predict'
# res = requests.post(url, json={'text': "I hate this movie!"})
# print(res.text)


# access and use the API
url = 'https://localhost:5000/predict'
res = requests.post(url, json={'text': "I hate this movie!"})
print(res.text)
# {"sentiment":"0"}
res = requests.post(url, json={'text': "I love this movie!"})
print(res.text)
# {"sentiment":"1"}
res = requests.post(url, json={'text': "I don't know how I feel about this movie!"})
print(res.text)

