def isToepliz(m):

	l = len(m[0])

	for i in range(len(m)-1):

		print m[i][:l-1]
		print m[i+1][1:]

		if m[i][:l-1] != m[i+1][1:]:

			return False

	return True

m = [
		[6,7,8,9,2],
		[4,6,7,8,9],
		[1,4,6,7,8],
		[0,1,4,6,7]
	]

print isToepliz(m)