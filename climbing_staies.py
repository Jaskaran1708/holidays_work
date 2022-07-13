def sol(a,b,count):
    if a==2 or a ==1:
        if a== 2:
            print(b*100+11)
            print(b*10+2)
            count += 1
        else:
            print(b*10+1)
            count += 1 
        return count
    else:
        count = sol(a-1,b*10+1,count+1) + count
        count = sol(a-2,b*10+2,count+1) + count

n = 3
print(sol(n,0,0))
