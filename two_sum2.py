a = [3,4,5,6,7,8,2]
n = len(a)
target = 13
for i in range(0,n):
    for j in range(i+1, n):
        if a[i] + a[j] == target:
            print(i,j)