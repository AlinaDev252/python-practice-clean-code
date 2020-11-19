a = [1, 5, 2, 22, -1, 4, 1]

b = [1, 3, -1, 4, -1]


x = -100000000
for i in a:
  if i > x:
    x = i

y = -100000000
for i in b:
  if i > y:
    y = i

print(y+x)