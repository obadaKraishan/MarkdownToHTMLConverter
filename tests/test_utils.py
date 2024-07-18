import unittest
from markdown_to_html_converter.utils import load_css, load_template

# Test case for the utility functions in utils.py
class TestUtils(unittest.TestCase):
    # Test method to check if the CSS loading function works correctly
    def test_load_css(self):
        # Load the default CSS
        css = load_css("default")
        # Assert that the loaded CSS contains the expected 'body' tag
        self.assertIn("body", css)

    # Test method to check if the template loading function works correctly
    def test_load_template(self):
        # Load the HTML template
        template = load_template()
        # Assert that the loaded template contains the placeholders for content and style
        self.assertIn("{content}", template)
        self.assertIn("{style}", template)

# Entry point for running the tests
if __name__ == "__main__":
    unittest.main()
