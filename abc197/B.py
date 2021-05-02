# -*- coding: utf-8 -*-
H, W, X, Y = map(int, input().split())

S = [input() for i in range(H)]

if S[X - 1][Y - 1] == '#':
  print(0)
  import sys
  sys.exit()

sum = 1

for s in reversed(S[X - 1][:Y - 1]):
  if s == '#':
    break
  sum += 1

for s in S[X - 1][Y:]:
  if s == '#':
    break
  sum += 1

for i in range(X - 1):
  s = S[X - 2 - i][Y - 1]
  if s == '#':
    break
  sum += 1

for i in range(X, H):
  s = S[i][Y - 1]
  if s == '#':
    break
  sum += 1

print(sum)

"""
3 3 2 2
...
.#.
...

0
"""


"""
3 3 1 1
...
...
...

5
"""

"""
3 3 3 3
...
...
...

5
"""

"""
4 4 2 2
##..
...#
#.#.
.#.#

4
"""

"""
3 5 1 4
#....
#####
....#

4
"""

"""
5 5 4 2
.#..#
#.###
##...
#..#.
#.###

3
"""