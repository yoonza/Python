num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N,B = input().split()
answer = 0

for i, n in enumerate(N[::1]):
		answer += int(B) ** i * num.index(n)
print(answer)