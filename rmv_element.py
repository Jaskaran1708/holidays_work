a=[]
n = int(input("no. of elements "))
for i in range(0,n):
    l = int(input())
    a.append(l)
print(a)
x = int(input("enter the no. to be deleted "))
d=[]
for i in a:
    if i != x:
        d.append(i)
print(d)

