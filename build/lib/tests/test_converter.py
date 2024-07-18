import unittest
from markdown_to_html_converter.converter import convert_markdown_to_html

class TestConverter(unittest.TestCase):
    def test_conversion(self):
        md_text = "# Hello World"
        html = convert_markdown_to_html(md_text, "default")
        self.assertIn("<h1>Hello World</h1>", html)

if __name__ == "__main__":
    unittest.main()
