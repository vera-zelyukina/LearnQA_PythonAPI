import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

count = len(response.history)
print(count)

last_response = response
print(last_response.url)
