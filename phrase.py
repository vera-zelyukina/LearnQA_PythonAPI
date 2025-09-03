class TestPhrase:
    def test_length(self):
        phrase = input("Set a phrase: ")
        expected_len = 15
        assert len(phrase) < expected_len, f"Длина фразы больше или равна {expected_len}"