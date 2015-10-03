import re
from class_def import parsed_line
from class_def import MAC_node
from oui import oui_lookup
import math

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
		x.oui_DA = oui_lookup(x.DA)
		x.oui_SA = oui_lookup(x.SA)
	else:
		x.ptype = '' #So that it will be skipped
	x.power = int((re.search(pattern_power,string)).group(0))		
	return x

def store(packet,dictionary):
	
	if packet.ptype == '':
		return
	add_edge(dictionary, packet.SA, packet.DA,packet.oui_SA, packet)
	add_edge(dictionary, packet.DA, packet.SA,packet.oui_DA, packet) 
	add_edge(dictionary, packet.SA, packet.name_sender, '', packet)
	add_edge(dictionary, packet.name_sender, packet.SA, '', packet)
	add_edge(dictionary, packet.DA, packet.name_sender,'', packet)
	add_edge(dictionary, packet.name_sender, packet.DA,'', packet)
	
def add_edge(dictionary, source, target, oui_type_source, packet):
	if not source in dictionary:
		dictionary[source] = MAC_node()
	if not target in dictionary[source].edges:
		dictionary[source].edges[target] = 0
	#Routines to update state of the object
	dictionary[source].edges[target] += 1
	dictionary[source].weight += 1
	update_coordinates(dictionary[source], packet.power)
	if dictionary[source].oui == '':
		dictionary[source].oui = oui_type_source
	
def update_coordinates(node_object, power):
	
	function = abs(power)
	division_const  = 10
	node_object.x =1/10* node_object.sign * math.sqrt(function/(1 + node_object.tan ** 2))
	node_object.y = node_object.tan * node_object.x

