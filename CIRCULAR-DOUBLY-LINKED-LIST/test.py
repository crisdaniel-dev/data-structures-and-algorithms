from circular_doubly import CircularDoubly

cd = CircularDoubly()

cd.add_first(5)
cd.add_first(2)
cd.add_last(9)
cd.add_last(12)
print(cd.display())

cd.add_after(7, 5)
cd.add_before(4, 5)
print(cd.display())

print(cd.length())
print(cd.total())
print(cd.largest())
print(cd.smallest())
print(cd.count_occur(5))

cd.del_first()
cd.del_last()
print(cd.display())

cd.del_given(7)
print(cd.display())

reversed_list = cd.reverse()
print(reversed_list.display())
print(cd.display())

cd.sort_asc()
print(cd.display())

cd.sort_desc()
print(cd.display())

cd.del_even()
print(cd.display())

cd.delete_greater(5)
print(cd.display())
