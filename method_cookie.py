import requests

class TestMethodCookie:
    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)
        expected_cookie = response.cookies.get_dict()
        print(expected_cookie)
        assert "HomeWork" in expected_cookie, "Name cookie's is not correct"

        expected_text = "hw_value"
        actual_text = response.cookies["HomeWork"]
        assert expected_text == actual_text, "Cookie is not correct"


