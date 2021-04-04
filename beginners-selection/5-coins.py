# -*- coding: utf-8 -*-
A, B, C, X = [int(input()) for i in range(4)]

count = 0
for a in range(A + 1):
  for b in range(B + 1):
    for c in range(C + 1):
      x = a * 500 + b * 100 + c * 50
      if x > X:
        continue
      elif X == x:
        count += 1

print(count)


"""
2
2
2
100

2
"""

"""
5
1
0
150

0
"""

"""
30
40
50
6000

213
"""
