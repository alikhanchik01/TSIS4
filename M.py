nums = list(map(int, input().split()))
odd = 0
even = 0
for num in nums:
    if num < 0:
        break
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"{round(even/(even+odd)*100,4)}% {round(odd/(even+odd)*100,4)}%")