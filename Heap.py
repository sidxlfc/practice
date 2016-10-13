class Node:

	def __init__(data) :

		this.data = data
		this.leftChild = None
		this.rightChild = None


class Heap:

	def __init__(self):

		self.heapList = [0]
		self.heapSize = 0
	
	def percUp(self, i):

		while i//2 > 0:

			if self.heapList[i//2] > self.heapList[i] :

				self.heapList[i//2] , self.heapList[i] = self.heapList[i] , self.heapList[i//2]

			i = i//2

	def insert(self, x):

		self.heapList.append(x)
		self.heapSize += 1
		self.percUp(self.heapSize)

h = Heap()

a = [10, 5, 6, 10, 19, 25, 34, 7, -6, 5, -99]

for i in range(len(a)):

	h.insert(a[i])

for i in range(len(h.heapList)):

	print h.heapList[i]