def search(arr, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            return search(arr, low, mid - 1, x)
        else:
            return search(arr, mid + 1, high, x)
    else:
        return False
a = [2,3,4,6,5]
a.sort()
n = len(a)
b = []
c=[]
for i in range(1,n+1):
    b.append(i)
for i in b:
    if search(a,0,n-1,i):
        continue
    else:
        c.append(i)
print(c)
