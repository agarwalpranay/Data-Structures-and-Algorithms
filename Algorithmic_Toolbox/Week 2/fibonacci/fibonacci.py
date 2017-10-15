# Uses python3
def calc_fib(n):
	store = []
	if n <= 1:
		return n
	else:
		store.append(0)
		store.append(1)
		for i in range(2,n + 1):
			f = store[i - 1] + store [i - 2]
			store.append(f)
		return store[n]

n = int(input())
print(calc_fib(n))
