import re
from class_def import parsed_line
from class_def import MAC_node

def parse(string):
	x = parsed_line
	bol = False
	P = []
	P.append('Beacon')
	P.append( 'Probe Response')
	P.append ('Probe Request')
	pattern_SA = 'SA:([^\s]+)'
	pattern_DA = 'DA:([^\s]+)'#group 1
	pattern_power = '\-[1-9]\d{0,2}' #group 0
	pattern_name = '\s\(([^)]+)\).*\s\(([^)]*)\)' #group 2
	for i in range(0,3):
		C = re.search(P[i],string)
		if (C):
			x.ptype = C.group(0)
			bol = True
			break
	if not bol:
		print("Undefined string: ")
		print(string)
		return x
	x.SA = (re.search(pattern_SA,string)).group(1)
	x.DA = (re.search(pattern_DA,string)).group(1)
	x.name = (re.search(pattern_name,string)).group(2)
	x.oui= (re.search(pattern_name,string)).group(1)
	x.power = int((re.search(pattern_power,string)).group(0))		
	return x

def store(packet,dictionary):
	
	if packet.ptype == '':
		return
	add_edge(dictionary, packet.SA, packet.DA)
	add_edge(dictionary, packet.DA, packet.SA)
	add_edge(dictionary, packet.SA, packet.name)
	add_edge(dictionary, packet.name, packet.SA)
	add_edge(dictionary, packet.DA, packet.name)
	add_edge(dictionary, packet.name, packet.DA)
	
def add_edge(dictionary, source, target):
	if not source in dictionary:
		dictionary[source] = MAC_node()
	if not target in dictionary[source].edges:
		dictionary[source].edges[target] = 0
	dictionary[source].edges[target] += 1
	dictionary[source].weight += 1

