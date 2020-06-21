n = list(map(int, input().split()))
x, y = n.pop(0),n.pop(0)
x1, y1 = n.pop(0), n.pop(0)

while n:
 a,b = n.pop(0), n.pop(0)
 if x<=a<=x1 and y1<=b<=y:
  print('yes')
 else:
  print('no')