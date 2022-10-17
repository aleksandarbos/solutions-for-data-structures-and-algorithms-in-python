"""
C-6.23 Suppose you have three nonempty stacks R, S, and T. Describe a sequence
of operations that results in S storing all elements originally in T below all
of S’s original elements, with both sets of those elements in their original
order. The final configuration for R should be the same as its original
configuration. For example, if R = [1,2,3], S = [4,5], and T = [6,7,8,9],
the final configuration should have R = [1,2,3] and S = [6,7,8,9,4,5].
"""

import random

r = random.randint(3, 9)
s = random.randint(2, 8)
t = random.randint(4, 11)


R = [random.randint(0, 100) for _ in range(0, r)]
S = [random.randint(0, 100) for _ in range(0, s)]
T = [random.randint(0, 100) for _ in range(0, t)]


print(f'before R: {R}, S: {S}, T: {T}')

while len(S) > 0:
    R.append(S.pop())

while len(T) > 0:
    R.append(T.pop())

for i in range(0, t+s):
    S.append(R.pop())

print(f'after R: {R}, S: {S}, T: {T}')
