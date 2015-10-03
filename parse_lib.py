def parse(string):
	from packet_class import parsed_line
	import re
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
	x.power = int((re.search(pattern_power,string)).group(0))		
	return x
