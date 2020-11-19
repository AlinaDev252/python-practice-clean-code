a = [1, 5, 2, 22, -1, 21, 1, 0, 10]

x = 0
for i in a:
  if i % 3 == 0:
    x = x + i

y = 0
for j in a:
  if j % 2 == 0:
    y = y + j

z = 0
for s in a:
  if s % 5 == 0:
    z = z + s


print(x+y+z)