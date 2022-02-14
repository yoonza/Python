n = int(input())
for i in range(n):
  num  = input()
  score = 0
  count = 0
for j in range(len(num)):
  if(num[j] == 'O'):
    count +=1
    score +=count
  elif num[j] == 'X'):
    count = 0
    score +=0
  print(score)
