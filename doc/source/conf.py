# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
from pbr.version import VersionInfo

repo_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(repo_path)
sys.path.insert(0, repo_path)

# import wexpect

os.environ['WEXPECT_SPAWN_CLASS'] = 'SpawnPipe'
autodoc_mock_imports = ["pywintypes", "win32process", "win32con", "win32file", "winerror",
    "win32pipe", "ctypes", "win32console", "win32gui"]

# from ctypes import windll



# -- Project information -----------------------------------------------------

project = 'wexpect'
copyright = '2020, Benedek Racz'
author = 'Benedek Racz'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
package_name='wexpect'
info = VersionInfo(package_name)
version = info.version_string()

# The full version, including alpha/beta/rc tags.
release = version



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinx.ext.autodoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']