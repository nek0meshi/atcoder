import math

def calc():
  N = input()
  
  zero_count = 0
  for n in reversed(N):
    if n != '0':
      break
    zero_count += 1
  
  N = N[:-zero_count] if zero_count > 0 else N

  for i in range(math.ceil(len(N) / 2)):
    if N[i] != N[-i - 1]:
      return 'No'
  return 'Yes'

def main():
  print(calc())

main()
