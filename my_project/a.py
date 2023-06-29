def calc_fact(n):
	if n == 1:
		return n
	return n*calc_fact(n-1)