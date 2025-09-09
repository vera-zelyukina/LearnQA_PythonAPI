import requests

url = "https://gist.github.com/KotovVitaliy/138894aa5b6fa442163561b5db6e2e26"
response = requests.get(url)
print(response.text)