def merge(a, b) :
	
	l3 = []

	while a and b:
		
		if a[0] > b[0] :
			
			l3.append(b[0])
			b.remove(b[0])

		else :
			
			l3.append(a[0])
			a.remove(a[0])

	while a :
		
		l3.append(a[0])
		a.remove(a[0])

	while b :
		
		l3.append(b[0])
		b.remove(b[0])

	return l3	

def mergesort(a):
	
	if len(a) == 1 :
		return a

	else :

		l1 = mergesort(a[0:len(a)/2])
		l2 = mergesort(a[len(a)/2:len(a)])
		#print l1
		#print l2
		#print "merge " + str(l1) + str(l2) + " = " + str(merge(l1, l2))
		return merge(l1, l2)


a = [5, 1, 10, 19, -5, 80, 13]
print mergesort(a)

print a