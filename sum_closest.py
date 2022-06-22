a=[]
n = int(input("no. of elements "))
for i in range(0,n):
    l = int(input())
    a.append(l)
print(a)
b=[]
q = int(input("enter the target "))
for i in a:
    for j in a:
        for k in a:
           b.append(i+j+k)
for i in range(0, len(b)):
    if b[i] - q is min 

