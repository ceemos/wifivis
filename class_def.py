import random
class parsed_line:
	ptype = ''
	SA = ''	
	DA = ''	
	name_sender = ''
	oui_DA = ''
	oui_SA = ''
	power = 0

class MAC_node: #SA will be the name of the instance, DA the edge
	def __init__(self):
		self.weight = 0
		self.x = random.random()
		self.y = random.random() 
		self.oui= ''
		self.edges = {}
		
