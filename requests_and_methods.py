import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method":"GET"})
print(response.text)
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method":"HEAD"})
print(response.text)

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = {"method":"GET"})
print(response.text)

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
methods = ["GET", "POST", "PUT", "DELETE"]
for method in methods:
    for test_method in methods:
        params = None
        data = None
        if method == "GET":
            params = {"method": test_method}
        else:
            data = {"method": test_method}

        response = requests.request(method=method, url=url, data=data, params=params)
        print(response.text)

