class HashTable :

	def __init__(self):

		self.size = 128
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put (self, key, data) :

		hashvalue = self.hashfunction(key, self.size)

		if self.slots[hashvalue] == None :

			self.slots[hashvalue] = key
			self.data[hashvalue] = data

		else :

			nextslot = self.rehash(hashvalue, self.size)

			while self.slots[nextslot] != None and self.slots[nextslot] != key :

				nextslot = self.rehash(nextslot, slef.size)

			if self.slots[nextslot] == None :

				self.slots[nextslot] = key
				self.data[nextslot] = data

			else :

				self.data[nextslot] = data

	def hashfunction(self, key, size) :

		return key % size

	def rehash(self, oldhash, size) :

		return (oldhash + 1)%size

	def get(self, key) :

		startslot = self.hashfunction(key, self.size)

		data = None
		stop = False
		found = False
		position = startslot

		while self.slots[position] != None and not found and not stop :

			if self.slots[position] == key :

				found = True
				data = self.data[position]

			else :

				position = self.rehash(position, self.size)
				
				if position == startslot :
				
					stop = True

		return data

	def __getitem__(self, key) :

		return self.get(key)

	def __setitem__(self, key, data):

		self.put(key, data)

h = HashTable()

h[1] = "First Entry"
h[2] = "Second Entry"

print h[1]
print h[2]