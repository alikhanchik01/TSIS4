dic = dict()
s = input()
new_s = ''
for ch in s:
 if ch not in dic:
  new_s+=ch 
  dic[ch] = 1
print(new_s)