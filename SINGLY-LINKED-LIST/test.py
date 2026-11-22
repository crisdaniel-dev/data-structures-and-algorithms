from singly import Singly

s = Singly()
s.add_first(4)
s.add_first(3)
s.add_first(2)
s.add_last(9)
print(s.display())                      # 2 3 4 9
print(s.length())                       # 4
print(s.total())                        # 18
print(s.largest(), s.smallest())        # 9 2
r = s.reverse()
print(r.display())                      # 9 4 3 2
print(s.display())                      # 2 3 4 9  (the original did not change)
s.reverse_in_place()
print(s.display())                      # 9 4 3 2
s.del_given(3)
print(s.display())                      # 9 4 2
