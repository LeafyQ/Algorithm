class Stack(object):
	def __init__(self):
		self.s = []

	def isEmpty(self):
		return len(self.s)==0

	def size(self):
		return len(self.s)

	def top(self):
		return self.s[-1]

	def pop(self):
		if len(self.s)==0:
			raise Exception("The Stack is empty!")
			return None
		else:
			return self.s.pop()

	def push(self,elem):
		self.s.append(elem)


if __name__ == '__main__':
	s = Stack()
	for i in range(5):
		s.push(i)

	while not s.isEmpty():
		print('Popping ',s.pop(),'Current Size: ',s.size())