import re
from class_def import parsed_line
from class_def import MAC_node
import pdb
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
	pattern_name = '\s\(([^)]*)\).*\s\(([^)]*)\).*\s\(([^)]*)\)' #group 1,2,3(oui receiver, oui sender, name sender)
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
	temp = re.search(pattern_name,string)
	x.SA = (re.search(pattern_SA,string)).group(1)
	x.DA = (re.search(pattern_DA,string)).group(1)
	if temp:
		x.name_sender = temp.group(3)
		x.oui_DA= temp.group(1)
		x.oui_SA= temp.group(2)
	else:
		x.ptype = '' #So that it will be skipped
	x.power = int((re.search(pattern_power,string)).group(0))		
	return x

def store(packet,dictionary):
	
	if packet.ptype == '':
		return
	add_edge(dictionary, packet.SA, packet.DA,packet.oui_SA)
	add_edge(dictionary, packet.DA, packet.SA,packet.oui_DA)
	add_edge(dictionary, packet.SA, packet.name_sender, '')
	add_edge(dictionary, packet.name_sender, packet.SA, '')
	add_edge(dictionary, packet.DA, packet.name_sender,'')
	add_edge(dictionary, packet.name_sender, packet.DA,'')
	
def add_edge(dictionary, source, target, oui_type_source):
	if not source in dictionary:
		dictionary[source] = MAC_node()
	if not target in dictionary[source].edges:
		dictionary[source].edges[target] = 0
	dictionary[source].edges[target] += 1
	dictionary[source].weights += 1
	if dictionary[source].oui == '':
		dictionary[source].oui = oui_type_source
	

