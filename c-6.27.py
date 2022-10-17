"""
C-6.27 Suppose you have a stack S containing n elements and a queue Q that is
initially empty. Describe how you can use Q to scan S to see if it contains a
certain element x, with the additional constraint that your algorithm must
return the elements back to S in their original order. You may only use S,
Q, and a constant number of other variables.
"""

import random
from queue import Queue

s = random.randint(4, 11)
S = [random.randint(0, 100) for _ in range(0, s)]

target = S[random.randint(0, s)]

Q = Queue()


