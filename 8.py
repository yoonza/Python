n = int(input())
storage = []

def push(storage,x):
  storage.append(x)

def pop(storage):
  if len(storage) == 0:
    return -1
  else:
    num = storage[0]
    del storage[0]
    return num

def size(storage):
  return len(storage)

def empty(storage):
  if len(storage)==0:
    return 1
  else:
    return 0

def front(storage):
  if len(storage) == 0:
    return -1
  else:
    return storage[0]

def back(storage):
   if len(storage) == 0:
    return -1
   else:
    return storage[-1]



for i in range(n): 

    s = input().split()

    if s[0] == "push":
       push(storage,int(s[1]))
    elif s[0] == "pop":
        print(pop(storage))
    elif s[0] == "size":
        print(size(storage))
    elif s[0] == "empty":
        print(empty(storageba))
    elif s[0] == "front":
        print(front(storage))
    elif s[0] == "back":
        print(back(storage))
print(storage)
