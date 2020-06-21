s = input()

dic = {
 'L': (-1,0),
 'R': (1,0),
 'U': (0,1),
 'D': (0,-1)
}
curr = (0,0)
for ch in s:
 x,y = curr 
 x1, y1 = dic[ch]
 curr=(x+x1,y+y1)

if curr == (0,0):
 print(True)
else:
 print(False)