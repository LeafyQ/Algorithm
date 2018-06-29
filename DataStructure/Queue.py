class Queue(object):
	def __init__(self):
		self.q = []

	def isEmpty(self):
		return len(self.q)==0

	def size(self):
		return len(self.q)

	def front(self):
		return self.q[0]

	def pop(self):
		if len(self.q)==0:
			raise Exception("The Queue is empty!")
			return None
		else:
			del self.q[0]

	def push(self,elem):
		self.q.insert(0,elem)

if __name__ == '__main__':
	q = Queue()
	for i in range(5):
		q.push(i)

	while not q.isEmpty():
		q.pop()
		print('Dequing... Current Size: ',q.size())

