a= [6,5,4,4]
inc = 0
dec = 0
for i in range(0,len(a)-1):
    if a[i+1] > a[i]:
        inc += 1
    elif a[i+1] < a[i]:
        dec += 1
    else:
        inc += 1
        dec += 1
print(dec)
if inc == len(a)-1 or dec == len(a) -1 :
    print(True)
else :
    print(False)