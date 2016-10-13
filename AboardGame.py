class ABoardGame :

	def winner(self, m) :
	
		j = 0		
		n = len(m[0])
		i = n//2

		round = 1
		
		if n%2 == 0 :	
			
			i -= 1
			j = 1	
		

		while i >= 0 :
			
			print "round : ", round
			
			a = 0
			b = 0
			k = 0

			while k <= j:

				print "i = ", i
				print "j = ", j

				if m[i][i+k] == 'A' :
					a += 1
					m[i][i+k] = "."

				elif m[i][i+k] == 'B' :
					b += 1
					m[i][i+k] = "."

				if m[i+k][i+j] == 'A' :
					a += 1
					m[i+k][i+j] = "."

				elif m[i+k][i+j] == 'B' :
					b += 1
					m[i+k][i+j] = "."
				
				if m[i+k][i] == 'A' :
					a += 1
					m[i+k][i] = "."

				elif m[i+k][i] == 'B' :
					b += 1
					m[i+k][i] = "."

				if m[i+j][i+k] == 'A' :
					a += 1
					m[i+j][i+k] = "."

				elif m[i+j][i+k] == 'B' :
					b += 1
					m[i+j][i+k] = "."

				k += 1

			j += 2
			i -= 1
			
			print "a = ", a
			print "b = ", b

			if a > b :
				print a
				return "A"

			elif b > a :
				print b			
				return "B"

			a = 0
			b = 0

			round+=1

		return "Draw"

x = ABoardGame()

m = [
		["A", "A", "B"],
		["A", "A", "B"],
		["A", "A", "B"],
	]

print x.winner(m)
print m

m = [
		["A", "A", "B", "A"],
		["A", "A", "B", "A"],
		["A", "A", "B", "A"],
		["B", "B", "B", "B"],
	]

print x.winner(m)
print m