# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
a, b, c = map(int, input().split())
N = int(input())
arr_hm = [list(map(int, input().split())) for _ in range(N)]

# 到着最遅時刻、8:59
goal_latest_minutes = 8 * 60 + 59

# paiza駅に、遅くても到着している必要のある時刻
paiza_latest_minutes = goal_latest_minutes - c - b

for hour, minute in reversed(arr_hm):
  train_minutes = hour * 60 + minute
  if train_minutes <= paiza_latest_minutes:
    break

leave_latest_minues = train_minutes - a
leave_hours = leave_latest_minues // 60
leave_minutes = leave_latest_minues % 60

print('{:02}'.format(leave_hours) + ':' + '{:02}'.format(leave_minutes))
