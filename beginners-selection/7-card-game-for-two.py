# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

print(sum([val if index % 2 == 0 else -val for index, val in enumerate(sorted(A, reverse=True))]))

"""
2
3 1

2
"""

"""
3
2 7 4

5
"""

"""
4
20 18 2 18

18
"""

