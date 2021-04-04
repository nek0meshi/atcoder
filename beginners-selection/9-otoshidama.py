# -*- coding: utf-8 -*-

N, Y =  [int(i) for i in input().split()]

def calc():
  for n in range(N + 1):
    for m in range(N - n + 1):
      if Y == n * 10000 + m * 5000 + (N - n - m)  * 1000:
        return (n, m, N - n - m)

  return (-1, -1, -1)

print(*calc())

"""
9 45000

4 0 5
"""

"""
20 196000

-1 -1 -1
"""

"""
1000 1234000

14 27 959
"""

"""
2000 20000000

2000 0 0
"""
