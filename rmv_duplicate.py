a=[]
n = int(input("enter the no. of elements"))
for i in range(0,n):
    l = int(input())
    a.append(l)
print("origibal array",a)
res=[]
for i in a:
    if i not in res:
        res.append(i)
print("after removing duplictes",res)

