"""
R-6.14 Repeat the previous problem using the deque D and an initially empty
stack S.

prev problem:
R-6.13 Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8),
in this order. Suppose further that you have an initially empty queue Q.
Give a code fragment that uses only D and Q (and no other variables) and
results in D storing the elements in the order (1,2,3,5,4,6,7,8).
"""


from collections import deque

d = deque([1, 2, 3, 4, 5, 6, 7, 8])
s = []

print(d)

# s: 1, 2, 3, 8, 7, 6, 4, 5 # might be shorter if pushed: 8, 7, 6, 1, 2, 3, 5, 4 test out
s.append(d.popleft())
s.append(d.popleft())
s.append(d.popleft())
s.append(d.pop())
s.append(d.pop())
s.append(d.pop())
s.append(d.popleft())
s.append(d.popleft())

print(f's:{s}')


# d: 5, 4, 6, 7, 8, 3, 2, 1
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())

print(d)

# s: 1, 2, 3, 5, 4, 6, 7, 8
s.append(d.pop())
s.append(d.pop())
s.append(d.pop())
s.append(d.popleft())
s.append(d.popleft())
s.append(d.popleft())
s.append(d.popleft())
s.append(d.popleft())

print(f's:{s}')

# d: 8, 7, 6, 4, 5, 3, 2, 1
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())

print(d)

# s: 8, 7, 6, 4, 5, 3, 2, 1
s.append(d.popleft())
s.append(d.popleft())
s.append(d.popleft())
s.append(d.popleft())
s.append(d.popleft())
s.append(d.popleft())
s.append(d.popleft())

# d: 1, 2, 3, 5, 4, 6, 7, 8
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())
d.append(s.pop())

print(d)
