def recur(arr, acc):
  added = [acc + arr[0][0] * (i + 1) for i in range(arr[0][1])]
  if len(arr) == 1:
    return added
  else:
    return [
      *added,
      *recur(arr[1:], acc),
      *sum([recur(arr[1:], a) for a in added], [])
    ]

def calc(N, arr_a):
  arr_a.sort()

  # 数値の重複の際の計算量を落とすための前処理
  arr_with_count = []
  current = arr_a[0]
  index = 1
  count = 1
  while(True):
    if len(arr_a) == index:
      arr_with_count.append((current, count))
      break
    if arr_a[index] == current:
      count += 1
    else:
      arr_with_count.append((current, count))
      count = 1
      current = arr_a[index]
    index += 1

  result = sorted({0, *recur(arr_with_count, 0)})

  print(len(result))
  for r in result:
    print(r)

def main():
  N = int(input())
  arr_a = [int(input()) for _ in range(N)]
  # N = 100
  # arr_a = [1 for i in range(N)]
  calc(N, arr_a)

main()
