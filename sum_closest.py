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
            if i!=j and j != k and k!= i:
                b.append(abs(q -(i+j+k)))
print(min(b)+ q) 
