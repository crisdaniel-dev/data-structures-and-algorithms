from singly import Singly

s = Singly()

print("Empty:", s.display())

s.add_first(30)
s.add_first(20)
s.add_first(10)

print("After add_first:", s.display())

s.add_last(40)
s.add_last(50)

print("After add_last:", s.display())

print("Front:", s.front())
print("Rear:", s.rear())

s.add_before(30, 25)
print("After add_before:", s.display())

s.add_after(30, 35)
print("After add_after:", s.display())

s.del_first()
print("After del_first:", s.display())

s.del_last()
print("After del_last:", s.display())
