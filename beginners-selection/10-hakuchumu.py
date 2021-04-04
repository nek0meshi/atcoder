# -*- coding: utf-8 -*-

S = ''.join(reversed(input()))

dream = ''.join(reversed('dream'))
dreamer = ''.join(reversed('dreamer'))
erase = ''.join(reversed('erase'))
eraser = ''.join(reversed('eraser'))

while len(S) > 0:
  if S.startswith(eraser):
    S = S.replace(eraser, '', 1)
    continue
  elif S.startswith(dreamer):
    S = S.replace(dreamer, '', 1)
    continue
  elif S.startswith(dream):
    S = S.replace(dream, '', 1)
    continue
  elif S.startswith(erase):
    S = S.replace(erase, '', 1)
    continue
  else:
    print('NO')
    import sys
    sys.exit()

print('YES')


"""
erasedream

YES
"""

"""
dreameraser

YES
"""

"""
dreamerer

NO
"""
