import ctypes

def make_plaindrome(d):

	print d

	l = 0
	
	for k, v in d.iteritems():

		l += v

	l -= 1

	s = ''.join(['0'*l])

	s = ctypes.create_string_buffer(s)
	
	curr = 0

	for k, v in d.iteritems():

		if v%2 == 0:

			for i in range(0, v/2):

				s[curr+i] = k
				s[l-(curr+i)] = k
				print s.value
			
			curr += v/2

		else :

			for i in range(0, (v-1)/2):

				print curr, i
				s[curr+i] = k
				s[l-(curr+i)] = k
				print s.value
			
			curr += v/2

			s[l/2] = k

	return s.value


def longest_palindrome(s):

	d = {}

	for c in s:

		if c in d :

			d[c] += 1

		else :

			d[c] = 1

	count = 0
	key = ''

	for c in d :

		if d[c]%2 != 0 :

			if count < d[c] :

				if key:
					
					d[key] -= 1
					count = d[c]
					key = c

				else :
					count = d[c]
					key = c


			else :

				d[c] -= 1

	return make_plaindrome(d)

print longest_palindrome("acbeaebecededkjfdngskjfdngkjfdndkjfcddfdfs")
print longest_palindrome("ababc")