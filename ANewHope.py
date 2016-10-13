def count(f, l, d):
        
    z = l[0]
    x = f.index(z)
    z = 0
    
    if 0 == x :
    	return 1
    
    if len(f) - 1 - x >= d :
        return 1

    else :
    	return len(f)-1-x+d

f = [8,5,4,1,7,6,3,2]
l = [2,4,6,8,1,3,5,7]
d = 3

f = [1,2,3,4]
l = [4,3,2,1]
d = 3

print count(f,l,d)