def pattern_and_dictionary (p, d):

	pattern = []

	for i in range(len(p) - 1) :

		if ord(p[i+1]) < ord(p[i]) :

			pattern.append(-1)

		elif ord(p[i+1]) > ord(p[i]) :

			pattern.append(1)

		else :

			pattern.append(0)

	print pattern

	temp_pattern = []

	for x in d :

		if len(x) == len(p) :

			#print "Before : " + x

			for i in range(len(x) - 1) :

				#print i

				if ord(x[i+1]) < ord(x[i]) :

					temp_pattern.append(-1)

				elif ord(x[i+1]) > ord(x[i]) :

					temp_pattern.append(1)

				else :

					temp_pattern.append(0)

				#print temp_pattern

				if i <= len(x) - 2 :

					if pattern[i] != temp_pattern[i]:

						print "Not equal : " + str(temp_pattern)
						temp_pattern = []
						break

				if i == len(x) - 2 :

					print x
					temp_pattern = []

#pattern_and_dictionary("abc" , ["cdf", "too", "hgfdt" ,"paa"])

pattern_and_dictionary("acc" , ["cdf", "too", "hgfdt" ,"paa"])