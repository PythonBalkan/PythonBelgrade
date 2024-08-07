# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import json
import os

from sphinx.application import Sphinx

# -- Project information -----------------------------------------------------

project = "Python Belgrade"
copyright = "2024, Python Belgrade"
author = "Python Belgrade"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxcontrib.youtube",
    "sphinxcontrib.images",
    "sphinxcontrib.icon",
]

html_css_files = [
    "css/custom.css",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "shibuya"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_logo = "_static/img/logo-python-belgrade.png"
html_favicon = "_static/img/favicon.png"
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

with open("json-data/meetups.json") as file:
    meetups = json.load(file)

with open("json-data/speakers.json") as file:
    speakers = json.load(file)

html_context = {
    "meetups": meetups,
    "speakers": speakers,
}

if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True

html_theme_options = {
    "page_layout": "simple",
    "github_url": "https://github.com/pythonbalkan/pythonbelgrade",
    "linkedin_url": "https://www.linkedin.com/company/python-belgrade",
    "nav_links": [
        {
            "title": "Meetups",
            "url": "meetups/index",
        },
        {
            "title": "Speakers",
            "url": "speakers/index",
        },
        {
            "title": "Membership",
            "url": "membership/index",
        },
        {
            "title": "Sponsorship",
            "url": "sponsorship/index",
        },
        {
            "title": "Social",
            "children": [
                {
                    "title": "Telegram",
                    "url": "membership/telegram",
                },
                {
                    "title": "Meetup",
                    "url": "https://meetup.com/pythonbelgrade/",
                },
                {
                    "title": "Facebook",
                    "url": "https://www.facebook.com/python.belgrade/",
                },
            ],
        },
    ],
}


def more_context(app: Sphinx, docname: str, source: list) -> None:
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != "html":
        return
    src = source[0]
    rendered = app.builder.templates.render_string(src, {**app.config.html_context, **html_context})
    source[0] = rendered


def setup(app: Sphinx) -> None:
    """
    Setup

    Rendering rst using jinja

    Insert Google Analytics tracker
    Based on this Stackoverflow suggestion: https://stackoverflow.com/a/41885884
    """
    app.connect("source-read", more_context)
    app.add_js_file("https://www.googletagmanager.com/gtag/js?id=G-8DRV6SQ7NS")
    app.add_js_file("js/google_analytics_tracker.js")
