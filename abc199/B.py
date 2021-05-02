def calc():
  N = input()
  A = map(int, input().split())
  B = map(int, input().split())

  min_val = max(A)
  max_val = min(B)

  if max_val >= min_val:
    return max_val - min_val + 1
  else:
    return 0

def main():
  print(calc())

main()
