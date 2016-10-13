def find_neighbors(m, g, n, visited) :

	l = []

	if g[0] < n and g[1] < n and g[0] > 0 and g[1] > 0 :

		if m[g[0]][g[1]] < m[g[0] + 1][g[1]] :

			l.append([g[0] + 1, g[1]])

		if m[g[0]][g[1]] < m[g[0]][g[1] + 1] :

			l.append([g[0], g[1] + 1])

		if m[g[0]][g[1]] < m[g[0] - 1][g[1]] :

			l.append([g[0] - 1, g[1]])

		if m[g[0]][g[1]] < m[g[0]][g[1] - 1] :

			l.append([g[0], g[1] - 1])

	elif : 

		# so on..

	return l


def max_height(m, goals) :

	n = len(m[0]) - 1

	for g in goals :

		l = []

		visited = []
		l = find_neighbors(m, g, n, visited)

		while l :

			pointer = max(l)

			visited.append(pointer)

			l.remove(pointer)
			
			#temp.append(l)
			temp = []

			temp.append(max_height(m, find_neighbors(m, [pointer], n, visited)))

		return max(temp)

m = [[1,2,3,4],
    [2,3,4,5],
    [4,4,4,1],
    [1,2G,4,6]]

goals = [(2,1), (2,2)]

'''goal_paths = []
goal_origins = []

for g in goals :
	# [x,y,value]
	path = []
	# gets the path to origin with max length
	max_height(m,g,path)
	goal_paths.append(path)
	goal_origins.append(path[2])'''