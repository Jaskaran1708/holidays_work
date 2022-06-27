a=[]
n = int(input("enter the no. of elements"))
for i in range(0,n):
    l = int(input())
    a.append(l)
carry = 0
for i in reversed(a):
    print(a[n-i])
    if i != 9 and carry == 0:
        i = i + 1
        print(i)
    elif i == 9 and carry == 0:
        i = 0
        carry = 1
    elif i != 9 and carry == 1:
        i += 1
        carry = 0
    elif i == 9 and carry ==1:
        i = 0
        carry = 1
print(a)