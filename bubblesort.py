a = [5, 1, 10, 19, -5, 80, 13]

for j in range(0, len(a)):
	for i in range(j+1, len(a)):

		if a[j]>a[i]:
		
			temp = a[j]
			a[j] = a[i]
			a[i] = temp		

print a