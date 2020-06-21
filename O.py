n = int(input())
buildings = list(map(int,input().split()))
q = int(input())
for i in range(q):
 a,b = map(int,input().split())
 curr = buildings[a]
 can_see = 1
 while a<b:
  a+=1
  if buildings[a]>curr:
   curr = buildings[a]
   can_see +=1
 print(can_see)