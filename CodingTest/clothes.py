def solution(clothes):

	answer = 1

	c = {v[1] : [] for v in clothes}
	
	for cloth in clothes:
		c[cloth[1]].append(cloth[0])
	
	
	for k in c.keys():
		n = len(c[k])
		answer *= (n + 1)

	return answer - 1