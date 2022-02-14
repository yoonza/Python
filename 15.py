count = int(input())
for i in range(count):
    n = int(input())
    m = int(input())
    
    a = [list(range(1,m+1))]
    
    for k in range(1,n+1):
        a.append([])
        
        for A in range(m):
            if A == 0:
                a[k].append(1)
            else:
                a[k].append(a[k-1][A]+a[k][A-1])
        fore
    print(a[n][m-1])
