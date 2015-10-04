WifiVis
=======

You can't see them. You can't hear them. Yet they are talking all around you: Wifi devices.

![Noisy air at HackZurich.](doc/hackzurich-all.png?raw=true "Noisy air at HackZurich.")

WifiVis will visualize as much of the Wifi communication around you. At the moment this is mostly metadata: who is talking to whom? Who is asking for whom? who is talking most or loudest? 

# Dependencies

WifiVis uses a browser-based front end (atm only tested in Chrom(e|ium)) served by Flask. So you need Python 3 and Flask. It uses `tcpdump` for the packet parsing and `sudo` to gain root privileges. The MAC address vendor lookup uses Wireshark's database (tcpdump's is broken), and expects it in `/usr/share/wireshark/manuf`

WifiVis uses passive scanning to achieve that. You need to have a wifi adapter that supports monitor mode and put it monitor mode first. The `tcpdump` command used by WifiVis expects the monitor device at `mon0`, feel free to change that (in `wifivis.py`).

# Usage

First enable monitor mode by issuing `airmon-ng start <device>` (`airmon-ng` belongs to the `aircrack-ng` suite).

Configure parameter in the source code if needed, and run `python wifivis.py`. If prompt (might be not obviously visible) enter your `sudo` password (only for `tcpdump`, Python will run as your user).

Point a web browser at `http://localhost:5000/` and see how the connection graph develops. The graph shows devices with their MAC address and OUI, and network names, which are not physical things but names used by access points as well as clients.

Communication is shown by graph edges, weighted and color coded by the frequency of packets observed on that edge.

You can use the filter box in the top left corner to filter the graph for nodes matching a regular expression.

By default, WifiVis will listen on the channel that the adapter is configured to. To to channel hopping (which is useful to get a better overview), run an instance of `airodump-ng` in parallel.

The visualization is controlled by a number of parameters in the source code, mainly the total weight in `decay.py`. This determines how fast devices that are no longer heard will disappear from the graph, but note that high values might overload the web browser with to many nodes.

# History

This project was born on the HackZurich 2015 hackathon.