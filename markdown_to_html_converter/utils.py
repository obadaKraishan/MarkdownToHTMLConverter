import os

# Function to load the CSS content based on the provided style
def load_css(style):
    # Construct the path to the CSS file
    css_path = os.path.join(os.path.dirname(__file__), 'styles', f'{style}.css')
    # Open and read the CSS file, then return its content
    with open(css_path, 'r') as file:
        return file.read()

# Function to load the HTML template
def load_template():
    # Construct the path to the HTML template file
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'base.html')
    # Open and read the HTML template file, then return its content
    with open(template_path, 'r') as file:
        return file.read()
