###############################################################################
# Auto-generated by `jupyter-book config`
# If you wish to continue using _config.yml, make edits to that file and
# re-generate this one.
###############################################################################
import sys, os

sys.path.append(os.path.abspath('_ext'))
sys.path.append(os.path.abspath('_static'))

author = 'Pete Bankhead'
comments_config = {'hypothesis': False, 'utterances': False}
copyright = '2022-2023'
exclude_patterns = ['**.ipynb_checkpoints', '.DS_Store', 'Thumbs.db', '_build', '_unused/**', 'nbs/*']
extensions = ['sphinx_togglebutton', 'sphinx_copybutton', 'myst_nb', 'jupyter_book', 'sphinx_thebe', 'sphinx_comments', 'sphinx_external_toc', 'sphinx.ext.intersphinx', 'sphinx_design', 'sphinx_book_theme', 'sphinx_sitemap', 'notranslate_gui', 'sphinx_jupyterbook_latex']
external_toc_exclude_missing = False
external_toc_path = '_toc.yml'
gettext_compact = True
html_baseurl = 'https://bioimagebook.github.io/'
html_css_files = ['css/custom.css']
html_extra_path = ['./_static/google4a2104152fcec296.html']
html_favicon = ''
html_js_files = ['https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js', ['https://plausible.io/js/script.js', {'defer': 'defer', 'data-domain': 'bioimagebook.github.io'}]]
html_logo = 'images/book-logo-smaller.png'
html_sourcelink_suffix = ''
html_static_path = ['./_static']
html_theme = 'sphinx_book_theme'
html_theme_options = {'search_bar_text': 'Search this book...', 'launch_buttons': {'notebook_interface': 'classic', 'binderhub_url': 'https://mybinder.org', 'jupyterhub_url': '', 'thebe': True, 'colab_url': ''}, 'path_to_docs': '', 'repository_url': 'https://github.com/bioimagebook/bioimagebook.github.io', 'repository_branch': 'main', 'extra_footer': '<p>\nAll content is licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">CC-BY 4.0</a>, except where noted otherwise.\nSee <a href="https://bioimagebook.github.io/chapters/0-preamble/license.html" target="_blank">License & Reuse</a> for details.\n</p>\n', 'home_page_in_toc': True, 'announcement': '', 'analytics': {'google_analytics_id': ''}, 'use_repository_button': False, 'use_edit_page_button': False, 'use_issues_button': False}
html_title = 'Introduction to Bioimage Analysis'
language = 'en'
latex_engine = 'xelatex'
locale_dirs = ['locale/']
myst_enable_extensions = ['colon_fence', 'linkify', 'dollarmath', 'substitution', 'html_image']
myst_url_schemes = ['mailto', 'http', 'https']
nb_execution_allow_errors = False
nb_execution_cache_path = ''
nb_execution_excludepatterns = []
nb_execution_in_temp = False
nb_execution_mode = 'cache'
nb_execution_timeout = 30
nb_output_stderr = 'show'
numfig = True
pygments_style = 'sphinx'
suppress_warnings = ['myst.domains']
use_jupyterbook_latex = True
use_multitoc_numbering = True
