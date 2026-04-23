import os
import sys
from datetime import datetime

# Add the source directory to sys.path so sphinx can find 'dymion'
sys.path.insert(0, os.path.abspath('../../src'))

project = 'Dymion'
copyright = f'{datetime.now().year}, Elabsurdo984'
author = 'Elabsurdo984'
release = '0.5.0'

# Internationalization
language = 'en'  # Default language
locale_dirs = ['../locales/']   # Path to translation files
gettext_compact = False     # Use one .po file per source file

# Extensions
extensions = [
    'sphinx.ext.autodoc',       # Pull documentation from docstrings
    'sphinx.ext.viewcode',      # Add links to source code
    'sphinx.ext.napoleon',      # Support for Google/NumPy style docstrings
    'sphinx.ext.mathjax',       # Support for LaTeX math formulas
    'myst_parser',              # Support for Markdown
    'sphinx.ext.githubpages',   # Generate .nojekyll for GitHub Pages
]

# MyST configuration (Markdown)
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

# HTML output options
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
}
