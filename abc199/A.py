def calc():
  A, B, C = map(int, input().split())

  if A ** 2 + B ** 2 < C ** 2:
    return 'Yes'
  else:
    return 'No'

def main():
  print(calc())

main()
