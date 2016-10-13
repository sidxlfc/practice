class AlbertoTheAviator :
	
	def MaximumFlights(self, initial, duration, refuel) :

		newlist = []

		for i in range(len(duration)) :

			temp = (duration[i], refuel[i])

			newlist.append(temp)

		newlist.sort(key = lambda tup:tup[0])

		count = 0
		
		init = initial

		tlist1 = []
		tlist2 = []

		for i in range(len(newlist)) :

			if initial >= newlist[i][0] :

				initial = initial - newlist[i][0] + newlist[i][1]
				count += 1

			else : 

				tlist1.append(newlist[i])
		
		print tlist1

		while (True) :

			for i in range(len(tlist1)) :

				if initial >= tlist1[i][0] :

					initial = initial - tlist1[i][0] + tlist1[i][1]
					count += 1

				else : 

					tlist2.append(tlist1[i])


			if(tlist1 == tlist2) :
				print tlist1
				print tlist2
				break
				#return count

			tlist1 = []

			for i in range(len(tlist2)) :

				if initial >= tlist2[i][0] :

					initial = initial - tlist2[i][0] + tlist2[i][1]
					count += 1

				else : 

					tlist1.append(tlist2[i])

			if(tlist1 == tlist2) :
				break
				#return count

			tlist2 = []


		newlist.sort(key = lambda tup:tup[0], reverse = True)
		count2 = 0
		
		initial = init

		tlist1 = []
		tlist2 = []

		for i in range(len(newlist)) :

			if initial >= newlist[i][0] :

				initial = initial - newlist[i][0] + newlist[i][1]
				count2 += 1

			else : 

				tlist1.append(newlist[i])
		
		print tlist1

		while (True) :

			for i in range(len(tlist1)) :

				if initial >= tlist1[i][0] :

					initial = initial - tlist1[i][0] + tlist1[i][1]
					count2 += 1

				else : 

					tlist2.append(tlist1[i])


			if(tlist1 == tlist2) :
				print tlist1
				print tlist2
				break
				#return count2

			tlist1 = []

			for i in range(len(tlist2)) :

				if initial >= tlist2[i][0] :

					initial = initial - tlist2[i][0] + tlist2[i][1]
					count2 += 1

				else : 

					tlist1.append(tlist2[i])

			if(tlist1 == tlist2) :

				break
				#return count2

			tlist2 = []

		return max(count2, count)

A = AlbertoTheAviator()

print A.MaximumFlights(12, [4, 8, 2, 1], [2, 0, 0, 0])

print A.MaximumFlights(9, [4, 6], [0, 1])




















"""
init = initial

		for i in range(len(newlist)) :

			if initial >= newlist[i][0] :

				initial = initial - newlist[i][0] + newlist[i][1]
				count += 1

			else : 

				break

		print newlist

		count2 = 0

		initial = init

		for i in range(len(newlist)-1, -1, -1) :

			if initial >= newlist[i][0] :

				initial = initial - newlist[i][0] + newlist[i][1]
				count2 += 1

			else : 

				break

		newlist.sort(key = lambda tup:tup[1])

		#print newlist

		count3 = 0

		initial = init

		for i in range(len(newlist)-1, -1, -1) :

			if initial >= newlist[i][0] :

				initial = initial - newlist[i][0] + newlist[i][1]
				count3 += 1

			else : 

				break
				"""