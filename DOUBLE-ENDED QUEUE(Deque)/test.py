from deque import Deque

deque = Deque()
deque.add_front(20)
deque.add_front(10)
deque.add_rear(30)
deque.add_rear(40)

print(deque.display())
print(deque.remove_front())
print(deque.remove_rear())
print(deque.display())