from priority_queue import PriorityQueue

pq = PriorityQueue()

print("=== EMPTY QUEUE ===")
print(pq.is_empty())
print(pq.peek_data())
print(pq.peek_priority())
print(pq.display_all())
print(pq.count())

print("\n=== ENQUEUE ===")
pq.enqueue(3, "Carlo")
pq.enqueue(1, "Mark")
pq.enqueue(2, "John")
pq.enqueue(1, "David")
pq.enqueue(3, "Pedro")

print(pq.display_all())

print("\n=== DISPLAY PRIORITY ===")
print(pq.display_priority())

print("\n=== DISPLAY DATA ===")
print(pq.display_data())

print("\n=== PEEK ===")
print(pq.peek_data())
print(pq.peek_priority())

print("\n=== COUNT ===")
print(pq.count())

print("\n=== DEQUEUE ===")
print(pq.dequeue())
print(pq.dequeue())

print("\n=== AFTER DEQUEUE ===")
print(pq.display_all())

print("\n=== CLEAR ===")
pq.clear()

print(pq.display_all())
print(pq.is_empty())
print(pq.count())

print("\n=== ENQUEUE AFTER CLEAR ===")
pq.enqueue(2, "Ana")
pq.enqueue(1, "Luis")

print(pq.display_all())