# -*- coding: utf-8 -*-

N = int(input())

v = 1
count = 0
while(True):
  c = int(str(v) * 2)
  if c > N:
    break
  v += 1
  count += 1

print(count)
