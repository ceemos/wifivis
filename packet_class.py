import random
class parsed_line:
	ptype = ''
	SA = ''	
	DA = ''	
	name = ''
	power = 0

class MAC_node: #SA will be the name of the instance, DA the edge
	def __init__(self):
		self.weights = 0
		self.x = random.random()
		self.y = random.random() 
		self.edges = {}
	'''def is_edge(self,edge_id):
		return edge_id in self.edges
	def add_edge(self, edge_id):
		if is_edge(edge_id):
			self.edges[edge_id] += 1
		else:
			self.edges[edge_id] = 1'''
	
'''class name_node:
	def __init__(self):
		self.x = random.random()	
		self.y = random.random()
		self.count = 0
		self.edges = {}
	
	def is_edge(self,edge_id):
		return edge_id in self.edges
	def add_edge(self, edge_id):
		if is_edge(edge_id):
			self.edges[edge_id] += 1
		else:
			self.edges[edge_id] = 1'''

