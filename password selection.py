import requests

response = requests.post("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
password = response.text


while True:
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data= { "login": "super_admin", "password": password })
    test_cookie = response.json()["auth_cookie"]

    response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", data= { "cookie": test_cookie })
    if response.text != "You are NOT authorized":
        print(password, response.text)
        break
    else:
        response = requests.post("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
        password = response.text