# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import itertools

def calc():
  N, X = map(int, input().split())
  arr_x = [int(input()) for _ in range(N)]

  # 値段が安い順番に並び替える
  arr_x.sort()

  # 種類が最大になる場合の個数(count)を計算
  sum_price = 0
  for i, x in enumerate(arr_x):
    count = i
    sum_price += x
    if sum_price > X:
      break
  else:
    count = len(arr_x)

  max_price = 0
  for comb in itertools.combinations(arr_x, count):
    sum_comb = sum(comb)
    if sum_comb == X:
      return 0
    elif sum_comb < X:
      max_price = max(max_price, sum(comb))

  return X - max_price

def main():
  print(calc())

main()

"""
3 300
150
120
130

20
"""

"""
1 1000
1000

0
"""

"""
1 1000
1100

1000
"""


"""
3 300
200
120
130

50
"""