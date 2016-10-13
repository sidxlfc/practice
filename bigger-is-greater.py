# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

for bla in range(n) :
    
    s = raw_input()

    s = list(s)

    flag = False

    for i in reversed(range(len(s))) :
        
        if i > 0:

            #print "s of " + str(i) + " : " + s[i]
            #print "s of " + str(i-1) + " : " + s[i-1]

            if s[i] > s[i-1] :
                
                #print "in if"
                t = ''.join(sorted(s[i:]))

                t = list(t)

                print t

                j = 0
                for j in range(len(t)) :

                    if s[i-1] < t[j] :
                        
                        #print s[i-1]
                        #print t[j]
                        break

                s[i:] = t

                j = len(s) - len(t) + j

                s[i-1], s[j] = s[j], s[i-1]

                print ''.join(s)
                flag = True
                break

        else :
            break

    if not flag :
        print "no answer"