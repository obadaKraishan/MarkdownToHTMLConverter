from setuptools import setup, find_packages

# Setup configuration for the Markdown to HTML converter package
setup(
    # Name of the package
    name='markdown_to_html_converter',

    # Version of the package
    version='0.1',

    # Automatically find all packages in the project
    packages=find_packages(),

    # List of dependencies to install with this package
    install_requires=[
        'markdown2',  # Markdown to HTML conversion library
    ],

    # Include additional files specified in MANIFEST.in
    include_package_data=True,

    # Specify package data to include in the installation
    package_data={
        '': ['styles/*.css', 'templates/*.html'],  # Include CSS and HTML template files
    },

    # Define console scripts to create command-line commands
    entry_points={
        'console_scripts': [
            'md2html=markdown_to_html_converter.converter:main',  # Create 'md2html' command
        ],
    },
)
