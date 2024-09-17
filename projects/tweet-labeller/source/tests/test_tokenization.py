import unittest
from ..classifier.tokenizer import tokenize_text

class TestTokenizer(unittest.TestCase):
    def test_simple_sentence(self):
        text = "Hello, world!"
        expected = [["Hello", ",", "world", "!"]]
        self.assertEqual(tokenize_text(text), expected)

    def test_email(self):
        text = "Contact me at john.doe@example.com."
        expected = [["Contact", "me", "at", "john.doe@example.com", "."]]
        self.assertEqual(tokenize_text(text), expected)

    def test_phone_number(self):
        text = "My number is +1 (123) 456-7890."
        expected = [["My", "number", "is", "+1 (123) 456-7890", "."]]
        self.assertEqual(tokenize_text(text), expected)

    def test_emoticon(self):
        text = "I am happy :)"
        expected = [["I", "am", "happy", ":)"]]
        self.assertEqual(tokenize_text(text), expected)

    def test_multiple_cases(self):
        text = "Contact me at john.doe@example.com or call +1 (123) 456-7890. :)"
        expected = [
            ["Contact", "me", "at", "john.doe@example.com", "or", "call", "+1 (123) 456-7890", "."],
            [":)"]
        ]
        self.assertEqual(tokenize_text(text), expected)

    def test_multiple_emoticons(self):
        text = "I am happy :) and excited :D"
        expected = [["I", "am", "happy", ":)", "and", "excited", ":D"]]
        self.assertEqual(tokenize_text(text), expected)

if __name__ == '__main__':
    unittest.main()