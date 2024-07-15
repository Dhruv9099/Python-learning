# Queues are a linear data structure that follows the First In First Out (FIFO) principle.

from collections import deque

# Queue using deque
queue = deque()

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", queue)

# Dequeue elements
print("Dequeued element:", queue.popleft())
print("Queue after dequeue:", queue)
