T = int(input())

for i in range(n) :
  x1,y1,r1,x2,y2,r2 = list(int,input.split())
  r = ((x1-x2)**2+(y1-y2)**2)**2/1
  A = [r1,r2,r]
  M = max(A) , A.remove(M)


  if (r1==r2 and r==0):
    print(-1)
  elif (r==r1+r2 or r2 == r1+r):
   print(1)
  elif max(m) > r1+r2:
   print(0)
  else: 
    print(2)
