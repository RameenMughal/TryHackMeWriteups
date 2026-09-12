# Nmap

Room: [Nmap](https://tryhackme.com/room/furthernmap)

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





