a = [3,3,4,5,6,4,7]
b = [3,3,6,7,8,9]
n= len(a)
v = len(b)
for i in range(0,n):
    for j in range(0,v):
        if a[i] == b[j]:
            print(a[i])