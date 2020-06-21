n = int(input())
i = 0

while n>0:
 n-=i
 if n<=0:
  print('Bob')
  break
 n-=i*2
 if n<=0:
  print('Nelson')
  break
 i+=1