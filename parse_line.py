import re
import pdb
string = "03:32:35.298962 1.0 Mb/s 2472 MHz 11b -71dB signal antenna 1 BSSID:78:54:2e:49:ff:10 (oui Unknown) DA:80:e6:50:0c:98:40 (oui Unknown) SA:78:54:2e:49:ff:10 (oui Unknown) Probe Response (mycujoo.tv 1) [1.0* 2.0* 5.5* 11.0* 18.0 24.0 36.0 54.0 Mbit] CH: 13, PRIVACY"

string2 = "03:32:35.323715 1.0 Mb/s 2472 MHz 11b -85dB signal antenna 1 BSSID:Broadcast DA:Broadcast SA:80:e6:50:0c:98:40 (oui Unknown) Probe Request () [1.0 2.0 5.5 11.0 Mbit]"
M = []
pattern_name = '\s\(([^)]+)\).*\s\(([^)]*)\)' #group 2
pattern_power = '\-[1-9]\d{0,2}' #group 0
pattern_DA = 'DA:([^\s]+)' # group 1
pattern_SA = 'SA:([^\s]+)'

M.append( re.search(pattern,string))
M.append ( re.search(pattern,string2))

for i in range(0,2):
	if M[i]:
		print(M[i].group(1))
		pdb.set_trace()

