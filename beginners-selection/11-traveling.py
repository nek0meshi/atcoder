# -*- coding: utf-8 -*-

N = int(input())
TXY = [list(map(int, input().split())) for i in range(N)]

# 移動可能かどうか
# 最大移動可能量(= t)が、移動量(= x, yの差分の絶対値の和)より大きいこと
# かつ、最大移動可能量と移動量の奇偶が一致すること
# - 「その場にとどまることができない」ため、行ったり来たりして移動量を相殺できる必要がある
# が条件
def canMove(from_position, to_position):
  t_diff = to_position[0] - from_position[0]
  xy_diff = abs(to_position[1] - from_position[1]) + abs(to_position[2] - from_position[2])
  
  return t_diff >= xy_diff and t_diff % 2 == xy_diff % 2

# 現在位置、(t, x, y)
current = (0, 0, 0)

for p in TXY:
  if (not canMove(current, p)): 
    print('No')
    import sys
    sys.exit()
  current = p

print('Yes')


"""
5
3 1 2
6 1 1
7 1 2
10 4 2
20 4 2

Yes
"""


"""
1
2 100 100

No
"""

"""
2
5 1 1
100 1 1

No
"""