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







