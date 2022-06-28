a=[2,3,4,5,7]
n = len(a)
b = []
c=[]
for i in range(1,n+1):
    b.append(i)
for f in range(0,n):
    for j in range(0,n):
        if a[f] != b[j]:
            print(b)
            # c.append(a[f])
# for r in range(0,n):
#     for e in range(0,n):
#         if b[r] != c[e]:
#             print(b[r])


