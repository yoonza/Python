# 그릇 : 10
# 같은 방향 : 5 +
# 다른 : 10 +

pl = input()
h = 10

for i in range(1,len(pl)):
    if pl[i] == pl[i-1]:
        h += 5
    else:
        h += 10 

print(h)