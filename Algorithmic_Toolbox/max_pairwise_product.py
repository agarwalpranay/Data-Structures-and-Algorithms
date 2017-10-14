# Uses python3

result = 0

def max_pairwise(n, a):
	for i in range(0, n):
	    for j in range(i+1, n):
	        if a[i]*a[j] > result:
	            result = a[i]*a[j]
	return result


def max_pairwise_fast(n, a):
	max_index = -1
	for i in range(n):
		if max_index == -1 or a[i] > a[max_index]:
			max_index = i

	max_index2 = -1
	for i in range(n):
		if i != max_index and (max_index2 == -1 or a[i] > a[max_index2]):
			max_index2 = i

	return (a[max_index] * a[max_index2])


if __name__ == '__main__':
	n = int(input())
	a = [int(x) for x in input().split()]
	assert(len(a) == n)

	print(max_pairwise_fast(n, a))

