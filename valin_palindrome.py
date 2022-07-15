a = "aa"
b = a.lower()
c= []
for i in range(0,len(b)):
    if b[i] >= 'a' and b[i] <= 'z':
        c.append(b[i])
if len(c) == 1 or len(c) == 0:
    print(True)
for i in range(0,len(c)//2):
    if c[i] == c[len(c)-1-i]:
        continue
    else:
        break
if len(c)%2 == 0:
    print(len(c)//2)
    print(i)
    if i == len(c)//2 :
        print(True)
    else:
        print(False)
else:
    if i == len(c)//2-1 :
        print(True)
    else:
        print(False)
