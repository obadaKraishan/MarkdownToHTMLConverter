import unittest
from markdown_to_html_converter.converter import convert_markdown_to_html

# Test case for the Markdown to HTML converter
class TestConverter(unittest.TestCase):
    # Test method to check if the conversion is correct
    def test_conversion(self):
        # Sample Markdown text
        md_text = "# Hello World"
        # Convert Markdown to HTML using the default style
        html = convert_markdown_to_html(md_text, "default")
        # Assert that the resulting HTML contains the expected <h1> tag
        self.assertIn("<h1>Hello World</h1>", html)

# Entry point for running the tests
if __name__ == "__main__":
    unittest.main()
