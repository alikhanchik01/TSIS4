n,k = map(int, input().split())
maxx = 0
for i in range(n):
 num = max(list(map(int, input().split())))
 if maxx < num:
  maxx = num

if num >= k:
 print('YES')
else:
 print('NO')