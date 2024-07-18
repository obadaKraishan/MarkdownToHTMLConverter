
# 📝 Markdown to HTML Converter

A robust and flexible tool for converting Markdown files into HTML files. This application provides various themes and styles to enhance the HTML output, making it suitable for diverse use cases.

## 🌟 Features

- Converts Markdown to HTML with different styles and themes 🎨
- Easy-to-use command-line interface 🚀
- Customizable HTML templates for enhanced flexibility 📄

## 🛠️ Technologies Used

- **Frontend**: Not applicable (command-line interface)
- **Backend**: Python
- **Libraries**: `markdown2`

## 📝 Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/obadaKraishan/MarkdownToHTMLConverter.git
cd MarkdownToHTMLConverter
```

### 2. Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install .
```

### 4. Run the Application

Convert a Markdown file to HTML by running the following command:

```bash
md2html path/to/your_markdown.md -o path/to/output.html -t dark
```

## 📂 Project Structure

```
markdown_to_html_converter/
│
├── README.md                      # Project documentation
├── requirements.txt               # List of dependencies
├── setup.py                       # Setup configuration
│
├── markdown_to_html_converter/
│   ├── __init__.py
│   ├── converter.py               # Main conversion logic
│   ├── utils.py                   # Utility functions
│   ├── styles/
│   │   ├── __init__.py
│   │   ├── default.css            # Default CSS style
│   │   ├── dark.css               # Dark theme CSS style
│   │   └── light.css              # Light theme CSS style
│   └── templates/
│       ├── __init__.py
│       └── base.html              # Base HTML template
│
├── tests/
│   ├── __init__.py
│   ├── test_converter.py          # Tests for converter functions
│   └── test_utils.py              # Tests for utility functions
│
└── examples/
    └── example.md                 # Example markdown file for testing
```

## 🎨 Customization

### 1. Update CSS Styles

You can add or modify CSS styles in the `styles` directory to change the appearance of the HTML output.

### 2. Update HTML Templates

Customize the HTML templates in the `templates` directory to fit your needs.

### 3. Modify Conversion Parameters

Modify the conversion parameters in `converter.py` or use command-line arguments to change the input and output paths, as well as the theme.

## 📄 License

This project is developed by Obada Kraishan. If you have any questions or need further information, feel free to contact me at obada.kraishan@gmail.com.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributors

- [Obada Kraishan](https://github.com/obadaKraishan)
