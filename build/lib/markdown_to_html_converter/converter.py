import markdown2
import os
import argparse
from .utils import load_css, load_template


def convert_markdown_to_html(markdown_text, css_style):
    html_content = markdown2.markdown(markdown_text)
    css = load_css(css_style)
    template = load_template()
    return template.format(content=html_content, style=css)


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML")
    parser.add_argument("input", help="Input Markdown file")
    parser.add_argument("-o", "--output", help="Output HTML file", required=False)
    parser.add_argument("-t", "--theme", help="Theme for HTML output (default, dark, light)", default="default")

    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"Error: {args.input} does not exist.")
        return

    with open(args.input, 'r') as file:
        markdown_text = file.read()

    html_output = convert_markdown_to_html(markdown_text, args.theme)

    output_file = args.output or args.input.replace('.md', '.html')
    with open(output_file, 'w') as file:
        file.write(html_output)

    print(f"HTML file generated at {output_file}")


if __name__ == "__main__":
    main()
