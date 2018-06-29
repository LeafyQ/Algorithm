class Heap(object):
	def __init__(self,cmp = __lt__):
		self.data = [None,]
		self.size = 0
		self.cmp = cmp

	def isEmpty(self):
		return self.size == 0

	def HeapifyUp(self):
		pass

	def HeapifyDown(self):
		pass

	def buildHeap(self):
		pass

	def size(self):
		return self.size

	def insert(self,elem):
		self.data.append(elem)
		self.HeapifyUp()

	def removeMin(self):
		if self.size == 0 :
			raise Exception("Empty Heap!")
			return False
		self.data[1] = self.data[-1]
		self.data.pop()
		self.HeapifyDown()
		self.size-=1
		return True

	def heapSort():
		


if __name__ == '__main__':
	l = [2,5,3,6,11,13,7,0]


