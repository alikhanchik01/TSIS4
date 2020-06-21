import re
s = input()
if not re.match('^[a-z][a-z]*@[a-z][a-z]*\.[a-z][a-z]*',s):
 print('No') 
else:
 print('Yes')