import requests

endpoint = "http://localhost:8000/api/"
# endpoint = "https://httpbin.org/anything"

response = requests.get(endpoint, json={"Sup": "fellas"}, params={"q": 12})
print(response.text)
print(response.json())