import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, json={"title": "a"})
print(response.text)
print(response.status_code)
print(response.json()['message'])