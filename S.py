a, b = map(int, input().split())
s = input()
try:
 m,n = s.split('-')
 if len(m)==a and int(m) and int(n):
  print('Yes')
 else:
  print('No')
except ValueError:
 print('No')