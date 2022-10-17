"""
The indented parenthetic representation of a tree T is a variation
of the parenthetic representation of T that uses indentation and line breaks. Give an
algorithm that prints this representation of a tree.
"""

from lxml import etree as et

def parenthetic_tree(el, d=0, step=2):
    label = d * step * " " + el.tag
    print(label, end='')
    is_first_child = False

    for c in el.iterchildren():
        idx = el.index(c)
        l = len(el)

        if idx == 0: # first child
            is_first_child = True
            print(' (')
        elif idx != l:
            print(end='\n')
        parenthetic_tree(c, d+1, step=step)

    if is_first_child:
        closing_tag = "\n" + d * step * " " + ')'
        print(closing_tag, end='')

if __name__ == "__main__":
    tree = et.parse('./input/trees/bookstore.xml')
    root = tree.getroot()

    parenthetic_tree(root, step=4)

"""
bookstore.xml, step=4

bookstore (
    book (
        title
        author
        year
        price
        sign (
            test
            fest
        )
        ign (
            test
            fest
        )
    )
    book (
        title
        author
        year
        price
    )
    book (
        title
        author
        year
        price
    )
)
"""

"""
bin_tree_1.xml, step=2 (default)

root (
  one (
    one_1
    one_2 (
      one_2_1
      one_2_2
    )
  )
  two (
    two_1
    two_2
  )
)
"""
