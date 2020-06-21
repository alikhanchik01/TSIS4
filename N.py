a,b = map(int, input().split())


def op(a,b):
 if abs(b)>0:
  if b<0:
   return op(a-1,b+1)
  return op(a+1, b-1)
 return a

print(op(a,b))