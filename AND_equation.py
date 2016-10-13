def Yvalue(a) :

	split = len(a) - 1

	while split > 0 :

		result = a[0]&a[1]

		print a[split]

		for i in range(2,split) :
			print i, " = ", a[i]
			result = result&a[i]
			print "result = ", result

		print "---------------------------------------------------------------------------"
		
		for i in range(split + 1, len(a)) :
			print i, " = ", a[i]
			result = result&a[i]
			print "result = ", result

		if a[split] == result :

			return a[split]

		split -= 1

	return -1

a = [31,7,7]
b = [1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0, 0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1]
c = [191411,256951,191411,191411,191411,256951,195507,191411,192435,191411, 191411,195511,191419,191411,256947,191415,191475,195579,191415,191411, 191483,191411,191419,191475,256947,191411,191411,191411,191419,256947, 191411,191411,191411]

print Yvalue(c)