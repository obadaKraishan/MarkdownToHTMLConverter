import os

def load_css(style):
    css_path = os.path.join(os.path.dirname(__file__), 'styles', f'{style}.css')
    with open(css_path, 'r') as file:
        return file.read()

def load_template():
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'base.html')
    with open(template_path, 'r') as file:
        return file.read()
