# def insert():
#     a=[]
#     n = int(input("enter the no. of elements"))
#     for i in range(0,n):
#         l = int(input())
#         a.append(l)
#     b = sorted(a)
#     return b
# a = insert()
# b = insert()
# for i in range(0,n):
# print(a)
def insert():
    a=[]
    n = int(input("enter the no. of elements"))
    for i in range(0,n):
        l = int(input())
        a.append(l)
    b = sorted(a)
    return b
a=insert()
b = insert()
count = 0
c = []
for i in a:
    c.append(i)
for i in b:
    c.append(i)
print(sorted(c))