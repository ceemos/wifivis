import random
import math
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
		self.x = 0
		self.y = 0 
		self.oui= ''
		self.edges = {}
		self.theta = random.random() * 4.0 * math.pi  #Static const
