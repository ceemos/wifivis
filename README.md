WifiVis
=======

You can't see them. You can't hear them. Yet they are talking all around you: Wifi devices.

![Noisy air at HackZurich.](doc/hackzurich-all.png?raw=true "Noisy air at HackZurich.")

WifiVis will visualize as much of the Wifi communication around you as possible. At the moment this is mostly metadata: who is talking to whom? Who is asking for whom? Who is talking most or loudest? 

You can use it to see whether devices on your network are still alive, what other infrastructure is around and who is using up all the bandwidth. It does not need to know anything about your network or the sorts of protocols or devices used, as it will analyse metadata that all 802.11 devices cause. You can't hide from it.

The visualisation will give you an idea of how far the devices are away based on the signal strength; it might support triangulation using multiple devices of 802.11ac hardware in the future.

# Dependencies

WifiVis uses a browser-based front end (atm only tested in Chrom(e|ium)) served by Flask. So you need Python 3 and Flask. It uses `tcpdump` for the packet parsing and `sudo` to gain root privileges. The MAC address vendor lookup uses Wireshark's database (tcpdump's is broken), and expects it in `/usr/share/wireshark/manuf`

WifiVis uses passive scanning to achieve that. You need to have a wifi adapter that supports monitor mode and put it monitor mode first. The `tcpdump` command used by WifiVis expects the monitor device at `mon0`, feel free to change that (in `wifivis.py`).

# Usage

First enable monitor mode by issuing `airmon-ng start <device>` (`airmon-ng` belongs to the `aircrack-ng` suite).

Configure parameters in the source code if needed, and run `python wifivis.py`. If prompt (might be not obviously visible) enter your `sudo` password (only for `tcpdump`, Python will run as your user).

Point a web browser at `http://localhost:5000/` and see how the connection graph develops. The graph shows devices with their MAC address and OUI, and network names, which are not physical things but names used by access points as well as clients.

Communication is shown by graph edges, weighted and color coded by the frequency of packets observed on that edge.

You can use the filter box in the top left corner to filter the graph for nodes matching a regular expression.

By default, WifiVis will listen on the channel that the adapter is configured to. To do channel hopping (which is useful to get a better overview), run an instance of `airodump-ng` in parallel.

The visualization is controlled by a number of parameters in the source code, mainly the total weight in `decay.py`. This determines how fast devices that are no longer heard will disappear from the graph, but note that high values might overload the web browser with to many nodes.

# History

This project was born on the HackZurich 2015 hackathon.