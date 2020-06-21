a,b,c,d = map(int, input().split())
if a>b:
 a,b=b,a 
if c>d:
 c,d = d,c
if a>=c and b>=d:
 print('Thanks, Nurbek')
else:
 print('Impossible')