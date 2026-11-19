from circular_queue import CircularQueue

c = CircularQueue()

c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
# c.dequeue()
print(c.peek())
print(c.is_empty())
print(c.display())
print(c.g())