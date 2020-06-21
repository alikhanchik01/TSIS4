a,b = map(int, input().split())
for i in range(a):
 s=''
 for j in range(b):
  if (i+j)%2 == 0:
   s+='1'
  else:
   s+='0'
 print(s)