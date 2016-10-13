import random
import time

def quicksort(a) :
	
	if len(a) <= 1 :
		return a
	
	else :
		pivot = a[0]
		#print "pivot = " + str(pivot)

		for i in range(1, len(a)):

			if a[i] < pivot :
				#a = [a[i]] + a
				#print "before insert : " + str(a)
				a.insert(0, a[i])
				#print "after insert : " + str(a)
				a.pop(i+1)
				#print "after pop : " + str(a)

		pivotpos = a.index(pivot)
		return quicksort(a[:pivotpos]) + [a[pivotpos]] + quicksort(a[pivotpos+1:])
		#quicksort(a[pivotpos+1:len(a)])
		#return a

def qsort(arr): 
     if len(arr) <= 1:
          return arr
     else:
          return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

#a = [30, 19, 0, -2, 9, 6, 5, 10, 11, 12, 13]
a = []

for i in range (0, 1000000):
	
	a.append(random.random())

t1 = time.clock()
x = qsort(a)
t2 = time.clock()

print str(t2-t1)

#print quicksort(a)