import requests

class TestMethodHeader:
    def test_homework_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        expected_headers = {'Date': 'Mon, 08 Sep 2025 07:32:18 GMT', 'Content-Type': 'application/json', 'Content-Length': '15', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=10', 'Server': 'Apache', 'x-secret-homework-header': 'Some secret value', 'Cache-Control': 'max-age=0', 'Expires': 'Mon, 08 Sep 2025 07:32:18 GMT'}
        actual_headers = response.headers
        print(actual_headers)

        if len(actual_headers) < len(expected_headers):
            for key, value in actual_headers.items():
                assert key in expected_headers, f"Заголовок '{key}' отсутствует в ответе"
        elif len(actual_headers) > len(expected_headers):
                for key, value in expected_headers.items():
                    assert key in actual_headers, f"Заголовок '{key}' избыточный в ответе"
        else:
            for key, value in expected_headers.items():
                if key == "Date": continue
                if key == "Expires": continue
                assert actual_headers.get(key) == expected_headers.get(key), f"Значение '{key}' не корректное"
