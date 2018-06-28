class Node(object):
	def __init__(self,value):
		self.val =  value
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	def isEmpty(self):
		return self.head is None
		#return self.size == 0

	def Size(self):
		return self.size

	def Add(self,item):
		if isinstance(item,Node):
			item.next = self.head
			self.head = item
		else:
			newNode = Node(item)
			newNode.next = self.head
			self.head = newNode
		self.size +=1

	def Remove(self):
		if self.size == 0:
			raise Exception("The linkedList is empty!")
		else:
			self.head = self.head.next

	def Get(self,idx):
		count = 0
		if self.size < idx-1:
			raise Exception("Out of range")
			return None
		curr = self.head
		while count<idx:
			count+=1
			curr = curr.next
		return curr.val

	def __str__(self):
		s = ""
		count = 0
		curr = self.head
		while curr:
			s+='Node {0}: {1}\n'.format(count,curr.val)
			count+=1
			curr = curr.next
		return s

if __name__ == '__main__':
	print("Simple test:")
	ll = LinkedList()
	for i in range(5):
		ll.Add(i)
	print(ll)
	ll.Remove()
	print(ll)
	print(ll.Get(3))
