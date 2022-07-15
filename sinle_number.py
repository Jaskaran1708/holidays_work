a = [4,1,2,1,2]
a.sort()
stack = []
for i in range(0,len(a)):
    if len(stack) == 0:
        stack.append(a[i])
    else:
        if stack[len(stack)-1] == a[i]:
            stack.pop()
        else:
            stack.append(a[i])
print(stack[0])