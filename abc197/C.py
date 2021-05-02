# -*- coding: utf-8 -*-
# 未クリア
from functools import reduce

N = int(input())
A = list(map(int, input().split()))

def all_or(arr):
  return reduce(lambda x, y: x | y, arr)

def create_arr(carry, remaining):
  if len(remaining) == 1:
    return [*carry, [remaining[0]]]

  results = []
  for i in range(len(remaining) - 1):
    results.extend([create_arr(carry + [remaining[:i + 1]], remaining[i + 1:])])

  return results

arr = create_arr([], A)

print(arr)

res = map(lambda a: reduce(lambda x, y: x ^ y, map(all_or, a)), arr)

print(res)


"""
3
1 5 7

2
"""

"""
3
10 10 10

0
"""

"""
4
1 3 3 1

0
"""