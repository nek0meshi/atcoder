import math

def calc():
  A, B, W = map(int, input().split())

  min_val = math.ceil(W * 1000 / B)

  if min_val < 1:
    return 'UNSATISFIABLE'

  max_val = math.ceil(W * 1000 / A)

  return str(min_val) + ' ' + str(max_val)

def main():
  print(calc())

main()

