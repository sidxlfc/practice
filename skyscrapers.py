def pprint(rows):
    for r in rows:
        print(" ".join([str(i) for i in r]))

def step(x, y, rows, cols, N):

    #print('a', x,y, rows, cols)
    if (x >= N) or (y >= N):
        return False

    for i in range(1, N+1):
        if (i not in rows[x]) and (i not in cols[y]):
            rows[x].append(i)
            cols[y].append(i)
     #       print('b', x,y, rows, cols)

            if (x==N-1) and (y==N-1):
                pprint(rows)
                return True

            if (x+1 < N):
                nextx=x+1
                nexty=y
            else:
                nextx=0
                nexty=y+1

            if step(nextx,nexty,rows,cols,N) is True:
                return True

            rows[x].pop(-1)
            cols[y].pop(-1)

    return False

def build(N):

    rows = [[] for i in range(0,N)]
    cols = [[] for i in range(0,N)]

    step(0,0,rows,cols,N)

build(20)