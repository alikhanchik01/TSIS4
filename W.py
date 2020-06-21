n = int(input())
h = list(map(int, input().split()))
m = int(input())
count = 0
for height in h:
 if height>=m:
  count+=1

print(count)