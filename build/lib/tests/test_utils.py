import unittest
from markdown_to_html_converter.utils import load_css, load_template


class TestUtils(unittest.TestCase):
    def test_load_css(self):
        css = load_css("default")
        self.assertIn("body", css)

    def test_load_template(self):
        template = load_template()
        self.assertIn("{content}", template)
        self.assertIn("{style}", template)


if __name__ == "__main__":
    unittest.main()
