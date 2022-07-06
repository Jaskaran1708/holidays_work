a = [0,2,3,1,0]
n = len(a)
max = a[1]
index = 1
for i in range(1,n-1):
    if a[i]> max:
        max = a[i]
        index = i
print(index)