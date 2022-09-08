a = [7,6,5,4,3,2]
max = 0
min = min(a)
mini = 0
dec = 0
for i in range(0,len(a)):
    if a[i] == min:
        mini = i
for i in range(0,len(a)-1):
    if a[i] > a[i+1]:
        dec += 1
if dec == len(a)-1:
    print(0)
else:
    for i in range(mini,len(a)):
        if a[i] > max:
            max = a[i]
print(max - min)