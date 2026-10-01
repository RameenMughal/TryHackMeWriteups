# Nmap

Room: [Nmap](https://tryhackme.com/room/furthernmap)

Pre-requisite Room: [Introductory Networking](https://tryhackme.com/room/introtonetworking)

<img width="946" height="209" alt="image" src="https://github.com/user-attachments/assets/adc49678-372a-436b-aef0-09c894d29edf" />

## Deploy

Press the green button to deploy the machine!

I am using my Kali Linux Machine and connected to TryHackMe by OpenVPN command: `sudo openvpn FILENAME`

You can check the room [OpenVPN](https://tryhackme.com/room/openvpn) on how to connect.

## Introduction

When it comes to hacking, knowledge is power. The more knowledge you have about a target system or network, the more options you have available. This makes it imperative that proper enumeration is carried out before any exploitation attempts are made.

Say we have been given an IP (or multiple IP addresses) to perform a security audit on. Before we do anything else, we need to get an idea of the “landscape” we are attacking. What this means is that we need to establish which services are running on the targets. For example, perhaps one of them is running a webserver, and another is acting as a Windows Active Directory Domain Controller. The first stage in establishing this “map” of the landscape is something called port scanning. 

A domain controller is a dedicated server that runs Active Directory Domain Services (AD DS) to authenticate users, authorize access, and enforce security policies across a network domain.

When a computer runs a network service, it opens a networking construct called a “port” to receive the connection.  Ports are necessary for making multiple network requests or having multiple services available. For example, when you load several webpages at once in a web browser, the program must have some way of determining which tab is loading which web page. This is done by establishing connections to the remote webservers using different ports on your local machine. Equally, if you want a server to be able to run more than one service (for example, perhaps you want your webserver to run both HTTP and HTTPS versions of the site), then you need some way to direct the traffic to the appropriate service. Once again, ports are the solution to this. 

Network connections are made between two ports – an open port listening on the server and a randomly selected port on your own computer. For example, when you connect to a web page, your computer may open port 49534 to connect to the server’s port 443.

Every computer has a total of 65535 available ports; however, many of these are registered as standard ports. For example, a HTTP Webservice can nearly always be found on port 80 of the server. A HTTPS Webservice can be found on port 443. Windows NETBIOS can be found on port 139 and SMB can be found on port 445.

NetBIOS is an acronym for Network Basic Input/Output System. It provides services related to the session layer of the OSI model allowing applications on separate computers to communicate over a local area network.

Server Message Block (SMB) is a communication protocol intended to provide shared access to files and printers across nodes on a network of systems. It also provides an authenticated inter-process communication (IPC) mechanism.

If we do not know which of these ports a server has open, then we do not have a hope of successfully attacking the target; thus, it is crucial that we begin any attack with a port scan. This can be accomplished in a variety of ways – usually using a tool called nmap, which is the focus of this room.

Nmap can be used to perform many different kinds of port scan, the basic theory is this: nmap will connect to each port of the target in turn. Depending on how the port responds, it can be determined as being open, closed, or filtered (usually by a firewall). Once we know which ports are open, we can then look at enumerating which services are running on each port – either manually, or more commonly using nmap.

---

### Answer the questions below

1. What networking constructs are used to direct traffic to the right application on a server?

Ports

2. How many of these are available on any network-enabled computer?

65535

3. [Research] How many of these are considered "well-known"? (These are the "standard" numbers mentioned in the task)

1024

## Nmap Switches

Like most pentesting tools, nmap is run from the terminal. There are versions available for both Windows and Linux. Nmap is installed by default in both Kali Linux.

Nmap can be accessed by typing `nmap` into the terminal command line, followed by some of the "switches" (command arguments which tell a program to do different things) we will be covering below.

All you'll need for this is the help menu for nmap (accessed with `nmap -h`) and/or the nmap man page (access with `man nmap`)

<img width="419" height="356" alt="image" src="https://github.com/user-attachments/assets/ebfd7547-6968-4155-b768-c58302d79b23" />

---

### Answer the questions below

1. What is the first switch listed in the help menu for a 'Syn Scan' (more on this later!)?

`-sS`

2. Which switch would you use for a "UDP scan"?

`-sU`

3. If you wanted to detect which operating system the target is running on, which switch would you use?

`-O`

4. Nmap provides a switch to detect the version of the services running on the target. What is this switch?

`-sV`

5. The default output provided by nmap often does not provide enough information for a pentester. How would you increase the verbosity?

`-v`

6. Verbosity level one is good, but verbosity level two is better! How would you set the verbosity level to two?

(Note: it's highly advisable to always use at least this option)

`-vv`

We should always save the output of our scans -- this means that we only need to run the scan once (reducing network traffic and thus chance of detection), and gives us a reference to use when writing reports for clients.

7. What switch would you use to save the nmap results in three major formats?

`-oA`

The three main output formats Nmap provides for saving scan results:
- Normal format → `-oN`
- XML format → `-oX`
- Grepable format → `-oG`

So the switch that saves results in all three major formats at once is: `-oA`

8. What switch would you use to save the nmap results in a "normal" format?

`-oN`

9. A very useful output format: how would you save results in a "grepable" format?

`-oG`

Sometimes the results we're getting just aren't enough. If we don't care about how loud we are, we can enable "aggressive" mode. This is a shorthand switch that activates service detection, operating system detection, a traceroute and common script scanning.

10. How would you activate this setting?

`-A`

Nmap offers five levels of "timing" template. These are essentially used to increase the speed your scan runs at. Be careful though: higher speeds are noisier, and can incur errors!

11. How would you set the timing template to level 5?

`-T5`

We can also choose which port(s) to scan.

12. How would you tell nmap to only scan port 80?

`-p 80`

13. How would you tell nmap to scan ports 1000-1500?

`-p 1000-1500`

A very useful option that should not be ignored:

14. How would you tell nmap to scan all ports?

`-p-`

15. How would you activate a script from the nmap scripting library (lots more on this later!)?

`--script`

16. How would you activate all of the scripts in the "vuln" category?

`--script=vuln`

## Scan Types - Overview

When port scanning with Nmap, there are three basic scan types. These are:
- TCP Connect Scans (`-sT`)
- SYN "Half-open" Scans (`-sS`)
- UDP Scans (`-sU`)

Additionally there are several less common port scan types, some of which we will also cover (albeit in less detail). These are:
- TCP Null Scans (`-sN`)
- TCP FIN Scans (`-sF`)
- TCP Xmas Scans (`-sX`)

Most of these (with the exception of UDP scans) are used for very similar purposes, however, the way that they work differs between each scan. This means that, whilst one of the first three scans are likely to be your go-to in most situations, it's worth bearing in mind that other scan types exist.

## Scan Types - TCP Connect Scans

To understand TCP Connect scans (`-sT`), it's important that you're comfortable with the TCP three-way handshake. 

As a brief recap, the three-way handshake consists of three stages. First the connecting terminal (our attacking machine, in this instance) sends a TCP request to the target server with the SYN flag set. The server then acknowledges this packet with a TCP response containing the SYN flag, as well as the ACK flag. Finally, our terminal completes the handshake by sending a TCP request with the ACK flag set.

Well, as the name suggests, a TCP Connect scan works by performing the three-way handshake with each target port in turn. In other words, Nmap tries to connect to each specified TCP port, and determines whether the service is open by the response it receives.

For example, if a port is closed, [RFC 9293](https://datatracker.ietf.org/doc/html/rfc9293) states that:

*"... If the connection does not exist (CLOSED), then a reset is sent in response to any incoming segment except another reset. A SYN segment that does not match an existing connection is rejected by this means."*

If a port is closed, it means nothing is listening/accepting connections on that port. So, when a device receives a request (especially a SYN packet) to a closed port, it responds with a RST (Reset) packet.

In other words, if Nmap sends a TCP request with the SYN flag set to a closed port, the target server will respond with a TCP packet with the RST (Reset) flag set. By this response, Nmap can establish that the port is closed.

If, however, the request is sent to an open port, the target will respond with a TCP packet with the SYN/ACK flags set. Nmap then marks this port as being open (and completes the handshake by sending back a TCP packet with ACK set).

What if the port is open, but hidden behind a firewall?

Many firewalls are configured to simply drop incoming packets. Nmap sends a TCP SYN request, and receives nothing back. This indicates that the port is being protected by a firewall and thus the port is considered to be filtered.

That said, it is very easy to configure a firewall to respond with a RST TCP packet.

For example, in IPtables for Linux, a simple version of the command would be as follows:

`iptables -I INPUT -p tcp --dport <port> -j REJECT --reject-with tcp-reset`

The command tells the Linux firewall: “If someone tries to connect to this TCP port, reject the connection by sending back a TCP RST packet.” Unlike a firewall that silently drops the packet (which makes Nmap think the port is filtered), this firewall sends RST, which can make Nmap think the port is closed, even if a service is actually running behind the firewall.

---

### Answer the questions below

1. Which RFC defines the appropriate behaviour for the TCP protocol?

RFC 9293

2. If a port is closed, which flag should the server send back to indicate this?

RST

## Scan Types - SYN Scans

As with TCP scans, SYN scans (`-sS`) are used to scan the port-range of a target or targets; however, the two scan types work slightly differently. SYN scans are sometimes referred to as "Half-open" scans, or "Stealth" scans.

Where TCP scans perform a full three-way handshake with the target, SYN scans sends back a RST TCP packet after receiving a SYN/ACK from the server (this prevents the server from repeatedly trying to make the request). In other words, the sequence for scanning an open port looks like this:

<img width="272" height="234" alt="image" src="https://github.com/user-attachments/assets/454a4072-292f-4037-9d19-f0aa47ca02fc" />

<img width="1138" height="69" alt="image" src="https://github.com/user-attachments/assets/c7365ca9-e598-415d-a012-c314f78bd459" />

This has a variety of advantages for us as hackers:
- It can be used to bypass older Intrusion Detection systems as they are looking out for a full three way handshake. This is often no longer the case with modern IDS solutions; it is for this reason that SYN scans are still frequently referred to as "stealth" scans.
- SYN scans are often not logged by applications listening on open ports, as standard practice is to log a connection once it's been fully established. Again, this plays into the idea of SYN scans being stealthy.
- Without having to bother about completing (and disconnecting from) a three-way handshake for every port, SYN scans are significantly faster than a standard TCP Connect scan.

There are, however, a couple of disadvantages to SYN scans, namely:
- They require sudo permissions in order to work correctly in Linux. This is because SYN scans require the ability to create raw packets (as opposed to the full TCP handshake), which is a privilege only the root user has by default.
- Some services are fragile or unstable, and sending lots of SYN packets during a SYN scan (`-sS`) can sometimes cause those services to crash or stop working.

For this reason, SYN scans are the default scans used by Nmap if run with sudo permissions. If run without sudo permissions, Nmap defaults to the TCP Connect scan.

SYN scans can also be made to work by giving Nmap the `CAP_NET_RAW`, `CAP_NET_ADMIN` and `CAP_NET_BIND_SERVICE` capabilities; however, this may not allow many of the NSE scripts to run properly. These are Linux capabilities. Think of them as small, specific permissions that you can give a program instead of giving it full root privileges.

When using a SYN scan to identify closed and filtered ports, the exact same rules as with a TCP Connect scan apply.

If a port is closed then the server responds with a RST TCP packet. If the port is filtered by a firewall then the TCP SYN packet is either dropped, or spoofed with a TCP reset.

In this regard, the two scans are identical: the big difference is in how they handle open ports.

---

### Answer the questions below

1. There are two other names for a SYN scan, what are they?

Half-Open, Stealth

2. Can Nmap use a SYN scan without Sudo permissions (Y/N)?

N

## Scan Types - UDP Scans

Unlike TCP, UDP connections are stateless. This means that, rather than initiating a connection with a back-and-forth "handshake", UDP connections rely on sending packets to a target port and essentially hoping that they make it. This makes UDP superb for connections which rely on speed over quality (e.g. video sharing), but the lack of acknowledgement makes UDP significantly more difficult (and much slower) to scan. The switch for an Nmap UDP scan is (`-sU`)

When a packet is sent to an open UDP port, there should be no response. When this happens, Nmap refers to the port as being `open|filtered`. In other words, it suspects that the port is open, but it could be firewalled. If it gets a UDP response (which is very unusual), then the port is marked as `open`. More commonly there is no response, in which case the request is sent a second time as a double-check. If there is still no response then the port is marked `open|filtered` and Nmap moves on.

When a packet is sent to a closed UDP port, the target should respond with an ICMP (ping) packet containing a message that the port is unreachable. This clearly identifies closed ports, which Nmap marks as such and moves on.

Due to this difficulty in identifying whether a UDP port is actually open, UDP scans tend to be incredibly slow in comparison to the various TCP scans (in the region of 20 minutes to scan the first 1000 ports, with a good connection). For this reason it's usually good practice to run an Nmap scan with `--top-ports <number>` enabled. For example, scanning with  `nmap -sU --top-ports 20 <target>`. Will scan the top 20 most commonly used UDP ports, resulting in a much more acceptable scan time.

When scanning UDP ports, Nmap usually sends completely empty requests -- just raw UDP packets. That said, for ports which are usually occupied by well-known services, it will instead send a protocol-specific payload which is more likely to elicit a response from which a more accurate result can be drawn.

---

### Answer the questions below

1. If a UDP port doesn't respond to an Nmap scan, what will it be marked as?

`open|filtered`

2. When a UDP port is closed, by convention the target should send back a "port unreachable" message. Which protocol would it use to do so?

ICMP

## Scan Types - NULL, FIN and Xmas

NULL, FIN and Xmas TCP port scans are less commonly used than any of the others we've covered already. All three are interlinked and are used primarily as they tend to be even stealthier, relatively speaking, than a SYN "stealth" scan. 

Beginning with NULL scans:

- As the name suggests, NULL scans (`-sN`) are when the TCP request is sent with no flags set at all. As per the RFC, the target host should respond with a RST if the port is closed.
- FIN scans (`-sF`) work in an almost identical fashion; however, instead of sending a completely empty packet, a request is sent with the FIN flag (usually used to gracefully close an active connection). Once again, Nmap expects a RST if the port is closed.
- As with the other two scans in this class, Xmas scans (`-sX`) send a malformed TCP packet and expects a RST response for closed ports. It's referred to as an xmas scan as the flags that it sets (PSH, URG and FIN) give it the appearance of a blinking christmas tree when viewed as a packet capture in Wireshark.

In this context, a malformed TCP packet is a packet with an unusual combination of TCP flags that normally wouldn't be used for a regular connection. 

For an Xmas scan (-sX), Nmap sets:
- FIN - Finish/close the connection
- PSH - Push data now
- URG - Urgent data

all at the same time.

The expected response for open ports with these scans is also identical, and is very similar to that of a UDP scan. If the port is open then there is no response to the malformed packet. Unfortunately (as with open UDP ports), that is also an expected behaviour if the port is protected by a firewall, so NULL, FIN and Xmas scans will only ever identify ports as being `open|filtered`, `closed`, or `filtered`. If a port is identified as `filtered` with one of these scans then it is usually because the target has responded with an ICMP unreachable packet.

While RFC 793 mandates that network hosts respond to malformed packets with a RST TCP packet for closed ports, and don't respond at all for open ports; this is not always the case in practice. In particular Microsoft Windows (and a lot of Cisco network devices) are known to respond with a RST to any malformed TCP packet -- regardless of whether the port is actually open or not. This results in all ports showing up as being closed.

That said, the goal here is, of course, firewall evasion. Many firewalls are configured to drop incoming TCP packets to blocked ports which have the SYN flag set. By sending requests which do not contain the SYN flag, we effectively bypass this kind of firewall. Whilst this is good in theory, most modern IDS solutions are savvy to these scan types, so don't rely on them to be 100% effective when dealing with modern systems.

---

### Answer the questions below

1. Which of the three shown scan types uses the URG flag?

Xmas

2. Why are NULL, FIN and Xmas scans generally used?

Firewall Evasion

3. Which common OS may respond to a NULL, FIN or Xmas scan with a RST for every port?

Microsoft Windows

## Scan Types - ICMP Network Scanning

On first connection to a target network in a black box assignment, our first objective is to obtain a "map" of the network structure -- or, in other words, we want to see which IP addresses contain active hosts, and which do not.

One way to do this is by using Nmap to perform a so called "ping sweep". This is exactly as the name suggests: Nmap sends an ICMP packet to each possible IP address for the specified network. When it receives a response, it marks the IP address that responded as being alive. For reasons we'll see in a later task, this is not always accurate; however, it can provide something of a baseline and thus is worth covering.

To perform a ping sweep, we use the `-sn` switch in conjunction with IP ranges which can be specified with either a hypen (-) or CIDR notation. i.e. we could scan the 192.168.0.x network using: `nmap -sn 192.168.0.1-254` or `nmap -sn 192.168.0.0/24`

The `-sn` switch tells Nmap not to scan any ports -- forcing it to rely primarily on ICMP echo packets (or ARP requests on a local network, if run with sudo or directly as the root user) to identify targets. In addition to the ICMP echo requests, the `-sn` switch will also cause nmap to send a TCP SYN packet to port 443 of the target, as well as a TCP ACK (or TCP SYN if not run as root) packet to port 80 of the target.

---

### Answer the questions below

How would you perform a ping sweep on the 172.16.x.x network (Netmask: 255.255.0.0) using Nmap? (CIDR notation)

`nmap -sn 172.16.0.0/16`

## NSE Scripts - Overview

The Nmap Scripting Engine (NSE) is an incredibly powerful addition to Nmap. NSE Scripts are written in the Lua programming language, and can be used to do a variety of things: from scanning for vulnerabilities, to automating exploits for them. The NSE is particularly useful for reconnaisance, however, it is well worth bearing in mind how extensive the script library is.

There are many categories available. Some useful categories include:
- `safe`:- Won't affect the target
- `intrusive`:- Not safe: likely to affect the target
- `vuln`:- Scan for vulnerabilities
- `exploit`:- Attempt to exploit a vulnerability
- `auth`:- Attempt to bypass authentication for running services (e.g. Log into an FTP server anonymously)
- `brute`:- Attempt to bruteforce credentials for running services
- `discovery`:- Attempt to query running services for further information about the network (e.g. query an SNMP server).

A more exhaustive list can be found here [NSE Usage and Examples](https://nmap.org/book/nse-usage.html).

---

### Answer the questions below

1. What language are NSE scripts written in?

Lua

2. Which category of scripts would be a very bad idea to run in a production environment?

intrusive

## NSE Scripts - Working with the NSE

In Task 3 we looked very briefly at the `--script` switch for activating NSE scripts from the `vuln` category using `--script=vuln`. It should come as no surprise that the other categories work in exactly the same way. If the command `--script=safe` is run, then any applicable safe scripts will be run against the target (Note: only scripts which target an active service will be activated).

To run a specific script, we would use `--script=<script-name>` , e.g. `--script=http-fileupload-exploiter`.

Multiple scripts can be run simultaneously in this fashion by separating them by a comma. For example: `--script=smb-enum-users,smb-enum-shares`.

Some scripts require arguments (for example, credentials, if they're exploiting an authenticated vulnerability). These can be given with the `--script-args` Nmap switch. An example of this would be with the `http-put` script (used to upload files using the PUT method). This takes two arguments: the URL to upload the file to, and the file's location on disk.  For example: `nmap -p 80 --script http-put --script-args http-put.url='/dav/shell.php',http-put.file='./shell.php'`

Note that the arguments are separated by commas, and connected to the corresponding script with periods (i.e.  `<script-name>.<argument>`).

A full list of scripts and their corresponding arguments (along with example use cases) can be found here [NSE Scripts](https://nmap.org/nsedoc/scripts/).

Nmap scripts come with built-in help menus, which can be accessed using `nmap --script-help <script-name>`. This tends not to be as extensive as in the link given above, however, it can still be useful when working locally.

---

### Answer the questions below

1. What optional argument can the `ftp-anon.nse` script take?

`maxlist`

Check it from here [Script ftp-anon](https://nmap.org/nsedoc/scripts/ftp-anon.html) in Specific Arguments

## NSE Scripts - Searching for Scripts

Ok, so we know how to use the scripts in Nmap, but we don't yet know how to find these scripts.

We have two options for this, which should ideally be used in conjunction with each other. The first is the page on the Nmap website [NSE Scripts](https://nmap.org/nsedoc/scripts/) (mentioned in the previous task) which contains a list of all official scripts. The second is the local storage on your attacking machine. Nmap stores its scripts on Linux at `/usr/share/nmap/scripts`. All of the NSE scripts are stored in this directory by default -- this is where Nmap looks for scripts when you specify them.

There are two ways to search for installed scripts. One is by using the `/usr/share/nmap/scripts/script.db` file. Despite the extension, this isn't actually a database so much as a formatted text file containing filenames and categories for each available script.

<img width="470" height="116" alt="image" src="https://github.com/user-attachments/assets/a441c008-38bf-4ea2-a4e1-6cf32b0fbb42" />

Nmap uses this file to keep track of (and utilise) scripts for the scripting engine; however, we can also grep through it to look for scripts. 

For example: `grep "ftp" /usr/share/nmap/scripts/script.db`.

<img width="551" height="119" alt="image" src="https://github.com/user-attachments/assets/6132b02f-7e67-481b-bea2-a673353fb924" />

The second way to search for scripts is quite simply to use the `ls` command. For example, we could get the same results as in the previous screenshot by using `ls -l /usr/share/nmap/scripts/*ftp*`:

<img width="470" height="119" alt="image" src="https://github.com/user-attachments/assets/993761aa-c084-4e8f-87a5-89e0861f18b1" />

The same techniques can also be used to search for categories of script. 

For example: `grep "safe" /usr/share/nmap/scripts/script.db`

<img width="506" height="260" alt="image" src="https://github.com/user-attachments/assets/7dad29cd-49a8-4aab-a52e-a8c4a0471efd" />

---

### Installing new Scripts

We mentioned previously that the Nmap website contains a list of scripts, so, what happens if one of these is missing in the scripts directory locally? 

A standard `sudo apt update && sudo apt install nmap` should fix this; however, it's also possible to install the scripts manually by downloading the script from Nmap (`sudo wget -O /usr/share/nmap/scripts/<script-name>.nse https://svn.nmap.org/nmap/scripts/<script-name>.nse`). This must then be followed up with `nmap --script-updatedb`, which updates the `script.db` file to contain the newly downloaded script.

It's worth noting that you would require the same "updatedb" command if you were to make your own NSE script and add it into Nmap.

---

### Answer the questions below

1. Search for "smb" scripts in the `/usr/share/nmap/scripts/` directory using either of the demonstrated methods. What is the filename of the script which determines the underlying OS of the SMB server?

`smb-os-discovery.nse`

Write command: `grep "smb" script.db"` under the `/usr/share/nmap/scripts/` directory

<img width="529" height="218" alt="image" src="https://github.com/user-attachments/assets/37257e65-d272-480f-909f-608f3828df52" />

2. Read through this script. What does it depend on?

`smb-brute`

<img width="524" height="335" alt="image" src="https://github.com/user-attachments/assets/38264753-f6a3-4fbd-b36f-dd852f9aa25a" />

## Firewall Evasion

We have already seen some techniques for bypassing firewalls (think stealth scans, along with NULL, FIN and Xmas scans); however, there is another very common firewall configuration which it's imperative we know how to bypass.

Your typical Windows host will, with its default firewall, block all ICMP packets. This presents a problem: not only do we often use ping to manually establish the activity of a target, Nmap does the same thing by default. This means that Nmap will register a host with this firewall configuration as dead and not bother scanning it at all.

Fortunately Nmap provides an option for this: `-Pn`, which tells Nmap to not bother pinging the host before scanning it. This means that Nmap will always treat the target host(s) as being alive, effectively bypassing the ICMP block; however, it comes at the price of potentially taking a very long time to complete the scan (if the host really is dead then Nmap will still be checking and double checking every specified port).

It's worth noting that if you're already directly on the local network, Nmap can also use ARP requests to determine host activity.

There are a variety of other switches which Nmap considers useful for firewall evasion. We will not go through these in detail, however, they can be found here [Firewall/IDS Evasion and Spoofing](https://nmap.org/book/man-bypass-firewalls-ids.html).

The following switches are of particular note:
- `-f`:- Used to fragment the packets (i.e. split them into smaller pieces) making it less likely that the packets will be detected by a firewall or IDS.
- An alternative to `-f`, but providing more control over the size of the packets: `--mtu <number>`, accepts a maximum transmission unit size to use for the packets sent. This must be a multiple of 8.
- `--scan-delay <time>ms`:- used to add a delay between packets sent. This is very useful if the network is unstable, but also for evading any time-based firewall/IDS triggers which may be in place.
- `--badsum`:- this is used to generate in invalid checksum for packets. Any real TCP/IP stack would drop this packet, however, firewalls may potentially respond automatically, without bothering to check the checksum of the packet. As such, this switch can be used to determine the presence of a firewall/IDS.

---

### Answer the questions below

1. Which simple (and frequently relied upon) protocol is often blocked, requiring the use of the `-Pn` switch?

ICMP

2. [Research] Which Nmap switch allows you to append an arbitrary length of random data to the end of packets?

`--data-length`

## Practical

I am using my Kali Linux Machine to connect through OpenVPN. You can check the [OpenVPN](https://tryhackme.com/room/openvpn) room in TryHackMe.

Command: `sudo openvpn FILENAME`

---

### Answer the questions below

1. Does the target ip respond to ICMP echo (ping) requests (Y/N)?

N

<img width="347" height="65" alt="image" src="https://github.com/user-attachments/assets/afd81a6f-4cc9-41e2-aebd-4e765d8d5948" />

2. Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered?

999

Command: `nmap -sX -Pn -p 1-999 TARGET_IP`

<img width="355" height="89" alt="image" src="https://github.com/user-attachments/assets/f50327ad-a9aa-478c-a4e8-7c5ec0708251" />

3. There is a reason given for this -- what is it?

Note: The answer will be in your scan results. Think carefully about which switches to use -- and read the hint before asking for help!

No response

Command: `nmap -vv -Pn -p 1-999 TARGET_IP`

<img width="492" height="255" alt="image" src="https://github.com/user-attachments/assets/ce8dc64f-1094-4b6c-996a-3cb65dd1d8b6" />

4. Perform a TCP SYN scan on the first 5000 ports of the target -- how many ports are shown to be open?

5

Command: `nmap -sS -Pn -p 1-5000 TARGET_IP`

<img width="335" height="140" alt="image" src="https://github.com/user-attachments/assets/9e83e374-7c9b-4ac1-8747-b3f0bea65266" />

5. Open Wireshark and perform a TCP Connect scan against port 80 on the target, monitoring the results. Make sure you understand what's going on. Deploy the ftp-anon script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)

Y

Choose the `tun0` network interface as it connects to TryHackMe

Start capturing packets by double-clicking the interface.

Let's do the first part: TCP Connect Scan

Then run in terminal: `nmap -sT -Pn -p 80 TARGET_IP`

<img width="341" height="100" alt="image" src="https://github.com/user-attachments/assets/988e937c-ba7b-4e31-8d02-7187e3b865e7" />

Stop the Wireshark capture after the scan finishes.

In Wireshark, use this display filter: `tcp.port == 80`

<img width="859" height="176" alt="image" src="https://github.com/user-attachments/assets/da32abf8-f966-4b98-a5fd-78879fcd95d1" />

Look at the TCP packets. You should see the basic TCP connection process:

Your machine → Target: SYN
Target → Your machine: SYN/ACK
Your machine → Target: ACK

With `-sT`, Nmap makes a normal TCP connection to the target using your computer's regular networking system. If the port is open, the connection is successfully established. So `-sT` = make a normal TCP connection and see if it succeeds.

Let's do the second part: Run the `ftp-anon` script

Write in terminal: `nmap -Pn -p 21 --script ftp-anon TARGET_IP`

<img width="344" height="116" alt="image" src="https://github.com/user-attachments/assets/6e425045-d4af-4f4c-965b-cc23c438efb3" />

It's a yes as it allows anonymous login.

## Conclusion

There are lots of great resources for learning more about Nmap on your own. Front and center are Nmaps own (highly extensive) docs [Nmap Network Scanning](https://nmap.org/book/) which have already been mentioned several times throughout the room. It would be highly advisable to use them as a point of reference, should you need it.













