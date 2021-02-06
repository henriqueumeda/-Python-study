a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a

print(c)
print(c.count(5))
print(c.index(8))

print(d)
print(d.index(2))
print(d.index(2, 4))
print(d.index(5, 1))
