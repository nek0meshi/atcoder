import math

def main():
  R, X, Y = map(int, input().split())

  XY = (X ** 2 + Y ** 2) ** (1/2)

  if XY < R:
    print(2)
  else:
    print(math.ceil(XY / R))

main()
