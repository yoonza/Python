Python 3.8.3rc1 (tags/v3.8.3rc1:802eb67, Apr 29 2020, 21:39:14) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Array = []

N,A = map(int,input().split()) 
cnt = 0
 
for i in range(1,N+1):
  if N % i == 0 : 
     Array.append(i)
  cnt += 1 

if A > len(Array):
  print(0)
else:
  print(Array[A-1])