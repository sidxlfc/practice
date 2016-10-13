def fib(n):
 
	# array declaration
	f = [0]*(n+1)

	# base case assignment
	f[1] = 1

	# calculating the fibonacci and storing the values
	for i in xrange(2 , n+1):
		f[i] = f[i-1] + f[i-2]
	
	return f[n]
 
# Driver program to test the above function
n = 9
print "Fibonacci number is " , fib(n)