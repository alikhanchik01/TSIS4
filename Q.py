n = input()
n, d = sum(list(map(int,n))),int(n[-1])
if n%d==0:
 print('Yes')
else:
 print('No')