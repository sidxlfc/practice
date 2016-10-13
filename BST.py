class Node :

	def __init__(self, data) :

		self.data = data
		self.lefChild = None
		self.rightChid = None

def buildTree(a) :

	if len(a) >= 1 : 

		mid = len(a)/2
		root = Node(a[mid])

		root.leftChild = buildTree(a[0:mid])
		root.rightChid = buildTree(a[mid+1:len(a)])

		return root

	else :

		return None

def printTree(root) :

	if root != None:


		printTree(root.leftChild)
		#for a given range -> if root.data > 5 and root.data < 30 :
		
		printTree(root.rightChid)
		print root.data
		
a = [10, 5, 6, 10, 19, 25, 34, 7, -6, 5, -99]
a.sort()

print a

root = buildTree(a)

printTree(root)