# -*- coding: utf-8 -*-

n = int(input())
numbers = list(map(int, input().split()))

count = 0

while True:
  if 0 in numbers or 1 in map(lambda x: x % 2, numbers):
    break
  count += 1
  numbers = list(map(lambda x: x // 2, numbers))

print(count)

"""
3
8 12 40

2
"""


"""
4
5 6 8 10

0
"""


"""
6
382253568 723152896 37802240 379425024 404894720 471526144

8
"""
