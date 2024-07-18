import markdown2
import os
import argparse
from .utils import load_css, load_template


# Function to convert Markdown text to HTML with the specified CSS style
def convert_markdown_to_html(markdown_text, css_style):
    # Convert Markdown text to HTML
    html_content = markdown2.markdown(markdown_text)
    # Load the specified CSS style
    css = load_css(css_style)
    # Load the HTML template
    template = load_template()
    # Format the template with the HTML content and CSS style
    return template.format(content=html_content, style=css)


# Main function to handle command-line arguments and convert the file
def main():
    # Set up argument parser for command-line usage
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML")
    parser.add_argument("input", help="Input Markdown file")
    parser.add_argument("-o", "--output", help="Output HTML file", required=False)
    parser.add_argument("-t", "--theme", help="Theme for HTML output (default, dark, light)", default="default")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if the input file exists
    if not os.path.isfile(args.input):
        print(f"Error: {args.input} does not exist.")
        return

    # Read the content of the input Markdown file
    with open(args.input, 'r') as file:
        markdown_text = file.read()

    # Convert the Markdown content to HTML with the specified theme
    html_output = convert_markdown_to_html(markdown_text, args.theme)

    # Determine the output file name
    output_file = args.output or args.input.replace('.md', '.html')
    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        file.write(html_output)

    # Print the location of the generated HTML file
    print(f"HTML file generated at {output_file}")


# Entry point for the script
if __name__ == "__main__":
    main()
