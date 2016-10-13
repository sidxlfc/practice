def fib_recur(n):

	if n == 1 :

		return 0

	elif n == 2 :

		return 1

	else :

		return fib_recur(n-1) + fib_recur(n-2)

def fib_iter(n) :

	i = 0
	j = 1
	number = 0

	if n == 1:

		return 0

	elif n == 2:

		return 1

	else:

		for k in range(n-2):

			number = i + j
			i = j
			j = number

	return number

print fib_recur(6)