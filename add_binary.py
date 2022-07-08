s = '1010'
s2 = '1011'
a = 0
b=0
sum = 0
ans = ' '
for i in range(len(s)-1,-1,-1):
    a = a+int(s[i])*pow(2,len(s)-i-1)
for i in range(len(s2)-1,-1,-1):
    b = b+int(s2[i])*pow(2,len(s2)-i-1)
sum = a+b
while sum!=0:
    r = sum%2
    ans = str(r)+ans
    sum = sum//2
print(ans)