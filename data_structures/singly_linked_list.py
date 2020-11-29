
class Node(object):
	"""Node"""
	def __init__(self, item):
		self.item = item
		self.next = None

class SinglyLinkedList(object):
	"""Singly Linked List"""
	def __init__(self,node = None):
		self._head = node

	def add(self, item):
		"""insert an element in the head"""
		node = Node(item)
		node.next = self._head
		self._head = node

	def append(self,item):
		"""insert an ele,ent in the end"""
		cur = self._head
		if not cur:
			self.add(item)
		"""define a pointer named 'cur'"""
		node = Node(item)
		while cur.next:
			cur = cur.next
		"""
		if the element pointed to by 'cur' is empty
		there is the end of linked_list
		so join the Node 'node'
		"""
		cur.next = node

	@property
	def isempty(self):
		"""check whether it is empty"""
		return self._head == None

	@property
	def length(self):
		"""get the length of it"""
		n = 0
		cur = self._head
		while cur:
			cur = cur.next
			n += 1
		return n

	def traverse(self):
		"""get all elements and return as a list"""
		cur = self._head
		if not cur:
			return None
		trav_li = []
		while cur:
			trav_li.append(cur.item)
			cur = cur.next
		return trav_li

	def insert(self, item, index):
		"""insert node(node=Node(item)) at 'index'"""
		n = self.length
		if index > n or index < -n-1:
			raise ValueError("'index' is invalid")
		if index < 0:
			index = index + n + 1
		if index == 0:
			self.add(item)
		elif index == n:
			self.append(item)
		else:
			node = Node(item)
			cur = self._head
			cur_num = 0
			while cur.next:
				cur_num += 1
				if cur_num == index:
					node.next = cur.next
					cur.next = node
				else:
					cur = cur.next

	def delete(self,index):
		"""delete the element at 'index'"""
		n = self.length
		if index > n-1 or index < -n:
			raise ValueError("'index' is invalid")
		if index < 0:
			index = index + n
		if index == 0:
			self._head = self._head.next
		else:
			cur = self._head
			cur_num = 1
			while cur_num != index:
				cur_num += 1
				cur = cur.next
			cur.next = cur.next.next


	def findit(self, index):
		"""find the 'index' and return it"""
		n = self.length
		if index > n - 1 or index < -n:
			raise ValueError("'index' is invalid")
		if index < 0:
			index = index + n
		cur = self._head
		cur_num = 0
		while cur_num != index:
			cur_num += 1
			cur = cur.next
		return cur.item