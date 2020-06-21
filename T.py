def isPalindrome(a,result = 0):
 if a == 0:
  return result
 result = result*10+a%10
 a = a//10
 return isPalindrome(a, result)

n = int(input())
res = []
for i in range(n):
 a = int(input())
 if a == isPalindrome(a,0):
  res.append('Yes')
 else:
  res.append('No')
for r in res:
 print(r)