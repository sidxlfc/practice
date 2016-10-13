def subarray_sum(a, low, high) :

	max_so_far = a[0]
	curr_max = a[0] 

	l = []

	il = 0

	p = 0
	q = 0

	for i in range(0, len(a)) :

		if max(curr_max + a[i], a[i]) == curr_max + a[i] :

			curr_max = curr_max + a[i]

			if curr_max <= high and curr_max >= low :
				
				q = i
				l.append(p, q)

			else :

				p = i

		#max_so_far = max(max_so_far, curr_max)



a = [10, 15, 19, -1, -10, 103, 63, 14, 0, 12]

print subarray_sum(a, 0, 10)