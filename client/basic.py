import requests

endpoint = "https://httpbin.org/anything"

response = requests.get(endpoint, json={"title": "a"})
print(response.json())