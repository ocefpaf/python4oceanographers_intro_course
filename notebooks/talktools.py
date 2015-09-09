import requests

from IPython.display import HTML, display


def prefix(url):
    prefix = '' if url.startswith('http') else 'http://'
    return prefix + url


def simple_link(url, name=None):
    name = url if name is None else name
    url = prefix(url)
    return '<a href="%s">%s</a>' % (url, name)


def html_link(url, name=None):
    return HTML(simple_link(url, name))


# Utility functions
def website(url, name=None, width='100%', height=450):
    html = []
    name = url if name == 'auto' else name
    if name:
        html.extend(['<div style="margin-bottom:10px">',
                     simple_link(url, name),
                     '</div>'])

    html.append('<iframe src="%s"  width="%s" height="%s">' %
                (prefix(url), width, height))
    html.append('</iframe>')
    return HTML('\n'.join(html))


def nbviewer(url=None, gist=None, name=None, width='100%', height=450):
    if url:
        return website('nbviewer.ipython.org/url/' + url, name, width, height)
    elif gist:
        return website('nbviewer.ipython.org/' + str(gist), name,
                       width, height)


def load_style(s):
    """Load a CSS stylesheet in the notebook by URL or file name.

    Examples::
        %load_style mystyle.css
        %load_style http://ipynbstyles.com/otherstyle.css
    """
    if s.startswith('http'):
        r = requests.get(s)
        style = r.text
    else:
        with open(s, 'r') as f:
            style = f.read()
    s = '<style>\n{style}\n</style>'.format(style=style)
    display(HTML(s))


def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magic_function(load_style)


if __name__ == '__main__':
    display(HTML(open('style.css').read()))
