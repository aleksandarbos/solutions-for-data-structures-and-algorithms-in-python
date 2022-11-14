D = """
An inverted file is a critical data structure for implementing a search engine or the index of a book.
Given a document D, which can be viewed as an unordered, numbered list of words,
an inverted file is an ordered list of words, L, such that, for each word w in L, we store the indices of the
places in D where w appears. Design an efficient algorithm for constructing L from D.
"""

# an efficient data structure for this would be SortedTableMap

import re

def inverted_file(D):
    """
    returns list L storing the indices of where certain
    words occurs within the document D.
    """

    L = {}
    for m in re.finditer(r'(\w+)', D): # O(n) ?? xD
        word = m.group()
        index = m.start()
        indices = L.get(word)

        if indices is None:
            L[word] = [index]
        else:
            L[word].append(index)
    return sorted(L.items()) # O(n*log(n))

L = inverted_file(D)
print(L)

"""
[('An', [1]), ('D', [121, 305, 378]), ('Design', [324]), ('Given', [104]), ('L', [231, 264, 371]), ('a', [21, 64, 96, 110]), ('algorithm', [344]), ('an', [147, 185, 205, 331]), ('appears', [315]), ('as', [144]), ('be', [134]), ('book', [98]), ('can', [130]), ('constructing', [358]), ('critical', [23]), ('data', [32]), ('document', [112]), ('each', [249]), ('efficient', [334]), ('engine', [73]), ('file', [13, 197]), ('for', [47,
245, 354]), ('from', [373]), ('implementing', [51]), ('in', [261, 302]), ('index', [87]), ('indices', [280]), ('inverted', [4, 188]), ('is', [18, 202]), ('list', [170, 216]), ('numbered', [161]), ('of', [93, 175, 221, 288]), ('or', [80]), ('ordered', [208]), ('places', [295]), ('search', [66]), ('store', [270]), ('structure', [37]), ('such', [234]), ('that', [239]), ('the', [83, 276, 291]), ('unordered', [150]), ('viewed', [137]), ('w', [259, 313]), ('we', [267]), ('where', [307]), ('which', [124]), ('word', [254]), ('words', [178, 224])]
"""
