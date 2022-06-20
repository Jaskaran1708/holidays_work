a = []
n = int(input("no. of elements in array"))
for i in range(0,n):
    l = int(input())
    a.append(l)
def max_(a,n):
    max_sum = a[0]
    cur_sum = a[0]
    for i in range(0,n):
        cur_sum = max(a[i], cur_sum + a[i])
        max_sum = max(max_sum, cur_sum)
    return max_sum
print("max contigous sum is ", max_(a,n))