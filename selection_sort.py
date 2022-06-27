a = [ 46,7,2,4,7 ]
n = len(a)
def sort(a, n):
    for i in range(n):
        min = i 
        for j in range(i+ 1, n):
            if a[j] < a[min]:
                min = j
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
sort(a, n)
print(a)