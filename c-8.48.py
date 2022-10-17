"""
given a proper binary tree T define the reflection of T to be the binary tree T' such that each
node v in T is also in T' but the left child of v in T is v's right child in T' and the right child of v
in T is v's left child in T'. Show that preorder traversal of proper binary tree T is the same as postorder traversal
of T's reflection but in reverser order.
"""

def inverse_t(el, t):

    for c in el.iterchildren():


