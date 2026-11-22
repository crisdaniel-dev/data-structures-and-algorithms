from doubly import Doubly

d = Doubly()

d.add_first(5)
d.add_first(2)
d.add_last(9)
d.add_last(12)
print(d.display())

d.add_after(7, 5)
d.add_before(4, 5)
print(d.display())

print(d.length())
print(d.total())
print(d.largest())
print(d.smallest())
print(d.count_occur(5))

d.del_first()
d.del_last()
print(d.display())

d.del_given(7)
print(d.display())

reversed_list = d.reverse()
print(reversed_list.display())
print(d.display())

d.sort_asc()
print(d.display())

d.sort_desc()
print(d.display())
