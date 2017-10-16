# Uses python3
import sys

def lcm_naive(a, b):
	for l in range(1, a*b + 1):
		if l % a == 0 and l % b == 0:
			return l
	return a*b

def gcd_smart(a, b):
	if a >= b:
		dividend = a
		divisor = b
	else:
		dividend = b
		divisor = a

	while divisor != 0:
		remainder = dividend % divisor
		dividend = divisor
		divisor = remainder

	return dividend

def lcm_smart(a, b):
	lcm = a * b // gcd_smart(a, b)
	return lcm


if __name__ == '__main__':
#	a = int(input())
#	b = int(input())
	input = sys.stdin.read()
	a, b = map(int, input.split())
	print(lcm_smart(a, b))



