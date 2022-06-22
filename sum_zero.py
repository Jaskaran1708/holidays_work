a=[]
n = int(input("no. of elements "))
for i in range(0,n):
    l = int(input())
    a.append(l)
print(a)
sum = 0
for i in a:
    for j in a:
        for k in a:
           if i+j+k == 0 and i != j and j != k and k != i:
                print(set(i,j,k))
