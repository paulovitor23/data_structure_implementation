from queue import Queue
from collections import deque

q = Queue()

q.get(1)
q.get(2)
q.get(3)

print(q.get())
print(q.get())
