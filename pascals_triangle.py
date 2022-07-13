from math import factorial


def c(a,b):
    return int(factorial(a)/(factorial(b)*factorial(a-b)))
a = [1]
b = [a]
a = [1,1]
n=5
b.append(a)
for i in range(1,n-1):
    a=[]
    for j in range(0,len(b[i])+1):
        a.append(c(len(b[i]),j))
    b.append(a)
print(b)