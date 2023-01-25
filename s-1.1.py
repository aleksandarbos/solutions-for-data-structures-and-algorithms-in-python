"""
exercise for using stacks for html validation
"""

def is_valid_html(html):
    s = []
    idx = 0

    for c in html:
        if c == '<':
            if html[idx+1] != '/':
                tag = html[idx+1:html.index('>', idx)]
                s.append(tag)
            else:
                tag = html[idx+2:html.index('>', idx)]
                if tag != s.pop():
                    return False
        idx += 1
    return len(s) == 0

if __name__ == "__main__":


    h0 = "<html><head><title>blablalb blall</title></head><body><a>best link ever</a></body></html>"

    h1 = """<html>
                <body>
                    <p>here's some ordinal text</p>
                    <div>
                        <p>nothing to see here</p>
                        <p>just another para</p>
                    </div>
                </body>
            </html>
        """

    h2 = """<div>
                <ul>
                    <li>test</li>
                    <li>invalid html
                <ul>
            </div>
        """

    h3 = """<div>
                <ul>
                    <li>test</ul>/li>
                    <li>invalid html</li>
            </div>
        """


    assert is_valid_html(h0)
    assert is_valid_html(h1)
    assert not is_valid_html(h2)
    assert not is_valid_html(h3)
