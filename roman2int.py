s = 'XXIX'
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
a =  []
count = 0
sum = 0
for i in s:
    if i == 'I':
        a.append( I)
        count += 1
    elif i == 'V':
        a.append( V)
        count += 1
    elif i == 'X':
        a.append( X)
        count += 1
    elif i == 'L':
        a.append( L)
        count += 1
    elif i == 'C':
        a.append( C)
        count += 1
    elif i == 'D':
        a.append( D)
        count += 1
    elif i == 'M':
        a.append( M)
        count += 1
print(a)
i = len(s)-1
while(i != 0):
    print(a[i])
    if a[i] <= a[i-1] :
        sum = sum+a[i] + a[i-1]
        i = i-2
    else:
        sum = sum+a[i] - a[i-1]
        i = i-2 
sum = sum + a[i]
print(sum)