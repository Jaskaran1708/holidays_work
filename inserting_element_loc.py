a=[]
n = int(input("enter the no. of elements"))
for i in range(0,n):
    l = int(input())
    a.append(l)
s = sorted(a)
def find_index(s,n,f):
    for i in range(n):
        if s[i] == f:
            return i
        elif s[i]>f:
            return i
    return n
f = int(input("enter the no. to be added"))
print(find_index(s,n,f))