a = [1,0,-1,0,-2,2]
n = len(a)
target = 0
for i in range(0,n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for s in range(k+1,n):
                if a[i] + a[j] + a[k] + a[s] == target:
                    print(a[i],a[j],a[k],a[s])