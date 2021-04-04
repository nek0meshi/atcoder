# -*- coding: utf-8 -*-

N, A, B = map(int, input().split())

def rowSum(n):
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  return sum

res = 0
for i in range(1, N + 1):
  res += i if A <= rowSum(i) <= B else 0

print(res)


"""
20 2 5

84
"""

"""
10 1 2

13
"""

"""
100 4 16

4554
"""
