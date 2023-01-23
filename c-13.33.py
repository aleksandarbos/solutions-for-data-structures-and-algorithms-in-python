"""
Let T be a text string of length n. Describe an O(n)-time method for
finding the longest prefix of T that is a substring of the reversal of T.
"""

def long_prefix_of_reversed(T):
    max_span, span = 0, 0
    for c in reversed(T):
        if c == T[span]:
            span += 1
            if span > max_span:
                max_span = span
        else:
            span = 0
    return T[:max_span]

if __name__ == "__main__":
    T = "wow kayak is the best thing from kayak wow can offer"
    assert long_prefix_of_reversed(T) == "wow kayak "

    T = "book is written by Poeob"
    assert long_prefix_of_reversed(T) == "bo"

    T = "gratitude, so overlooked, but so important"
    assert long_prefix_of_reversed(T) == "g"

    T = ""
    assert long_prefix_of_reversed(T) == ""
