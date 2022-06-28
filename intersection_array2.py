a= [2,3,4,5,6]
b =[2,2,7,8,5,5]
n = len(a)
v= len(b)
s= []
for i in range(0,n):
    for j in range(0,v):
        if a[i]== b[j]:
            s.append(a[i])
res=[]
for i in s:
    if i not in res:
        res.append(i)
print(res)

