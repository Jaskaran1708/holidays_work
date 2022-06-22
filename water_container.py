def insert():
    a=[]
    n = int(input("enter the no. of elements"))
    for i in range(0,n):
        l = int(input())
        a.append(l)
    b = sorted(a)
    return a
a=insert()
n = len(a)
b = []
gap = 0
for i in range(0,n-1):
    for j in range(i+1, n):
        gap = j - i
        b.append(gap * min(a[i],a[j]))
print(max(b))
