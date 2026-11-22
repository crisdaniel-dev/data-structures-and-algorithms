from circular import Circular

c = Circular()
for n in (7, 8, 9, 1, 2):
    c.add_first(n)
print(c.display())                 # 2 1 9 8 7
print(c.head(), c.tail())          # 2 7
c.add_last(5)
print(c.display())                 # 2 1 9 8 7 5
c.add_after(6, 7)
print(c.display())                 # 2 1 9 8 7 6 5
c.add_before(0, 2)
print(c.display())                 # 0 2 1 9 8 7 6 5
print(c.is_circular())             # True
c.del_first()
c.del_last()
c.del_given(9)
print(c.display())                 # 2 1 8 7 6

print(c.length())                  # 5
print(c.total())                   # 24
print(c.largest(), c.smallest())   # 8 1
print(c.reverse().display())       # 6 7 8 1 2
c.reverse_in_place()
print(c.display())                 # 6 7 8 1 2
