"""
R-6.13 Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8),
in this order. Suppose further that you have an initially empty queue Q.
Give a code fragment that uses only D and Q (and no other variables) and
results in D storing the elements in the order (1,2,3,5,4,6,7,8).
"""

from collections import deque
from queue import Queue

d = deque([1, 2, 3, 4, 5, 6, 7, 8])
q = Queue()

print(d)

# queue: 1, 2, 3, 8, 7, 6, 4, 5
q.put(d.popleft())
q.put(d.popleft())
q.put(d.popleft())
q.put(d.pop())
q.put(d.pop())
q.put(d.pop())
q.put(d.popleft())
q.put(d.popleft())

# dequeue: 1, 2, 3, 8, 7, 6, 4, 5
d.append(q.get())
d.append(q.get())
d.append(q.get())
d.append(q.get())
d.append(q.get())
d.append(q.get())
d.append(q.get())
d.append(q.get())
print(d)
assert list(d) == [1, 2, 3, 8, 7, 6, 4, 5]


# queue: 1, 2, 3, 5, 4, 6, 7, 8
q.put(d.popleft())
q.put(d.popleft())
q.put(d.popleft())
q.put(d.pop())
q.put(d.pop())
q.put(d.pop())
q.put(d.pop())
q.put(d.pop())

# dequeue: 1, 2, 3, 5, 4, 6, 7, 8
d.append(q.get())
d.append(q.get())
d.append(q.get())
d.append(q.get())
d.append(q.get())
d.append(q.get())
d.append(q.get())
d.append(q.get())

print(d)
assert list(d) == [1, 2, 3, 5, 4, 6, 7, 8]


