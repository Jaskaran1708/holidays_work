s = 'aaaaa'
s2 = 'aaaaaa'
count = 0
if len(s2) > len(s):
    print('-1')
else:
    for i in range(0,len(s)-len(s2)+1):
        if s[i:len(s2)+i] == s2:
            count = i
        else:
            count = -1
    print(count)