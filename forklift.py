import random

def sort(a) :

	b = [0 for i in range(len(a))]
	c = [0 for i in range(len(a))]
	
	#print "before", b
	#print len(b)
	
	for i in range(len(a)) :
		
		b[a[i]] = i
		#print a[i], i

	#print "after", b

	for i in range(len(a)) :

		c[i] = a[b[i]]
		#print i, a[i]
	return c

def sort2(a) :

	i = 0
	while (True) :
		
		if i < len(a)-1 :
			#print i
			#print "before", a[a[i]], a[i]
			a[len(a)-1] = a[a[i]]
			a[a[i]] = a[i]
			a[i] = a[len(a)-1]
			#print "after", a[a[i]], a[i]
			#print a
			i += 1

		else :
			break

	return a

a = [8,6,4,0,1,3,5,7,2]

a.append(-100000)

print a

print sort2(a)