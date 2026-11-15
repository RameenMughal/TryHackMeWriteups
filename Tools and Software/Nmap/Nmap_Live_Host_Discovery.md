# Nmap Live Host Discovery

Room: [Nmap Live Host Discovery](https://tryhackme.com/room/nmap01)

Learning Prerequisites: 
1. [Web Application Basics](https://tryhackme.com/room/webapplicationbasics)
2. [Intro to LAN](https://tryhackme.com/room/introtolan)

<img width="945" height="206" alt="image" src="https://github.com/user-attachments/assets/8ac25fd7-c1eb-4110-b590-77ca4ec0f306" />

## Introduction

Nmap, short for Network Mapper, is free, open-source software released under the GPL license, created by Gordon Lyon (Fyodor), a network security expert and open-source programmer. Nmap is an industry-standard tool for mapping networks, identifying live hosts, and discovering running services. Nmap’s scripting engine can further extend its functionality, from fingerprinting services to exploiting vulnerabilities. 

The GNU General Public License (GPL) is a widely used copyleft open-source software license created by Richard Stallman and the Free Software Foundation (FSF).

A Nmap scan usually goes through the steps shown in the figure below, although many are optional and depend on the command-line arguments you provide.

<img width="1200" height="552" alt="image" src="https://github.com/user-attachments/assets/34613b3a-0944-42ba-b233-3cb0126ece31" />

---

### Learning Objectives

When we want to target a network, we want to find an efficient tool to help us handle repetitive tasks and answer the following questions:
- Which systems are up?
- What services are running on these systems?

The first question about finding live computers is answered in this room.

## Subnetworks

A network segment is a group of computers connected using a shared medium. For instance, the medium can be an Ethernet switch or a Wi-Fi access point. 

In an IP network, a subnetwork is usually equivalent to one or more network segments connected to the same router. 

The network segment refers to a physical connection, while a subnetwork refers to a logical connection.

In the following network diagram, we have four network segments or subnetworks. Generally speaking, your system would be connected to one of these network segments/subnetworks. 

A subnetwork, or simply a subnet, has its own IP address range and is connected to a more extensive network via a router. Additionally, a firewall may be present between network segments, enforcing security policies on the traffic that passes between them.

<img width="1400" height="1400" alt="image" src="https://github.com/user-attachments/assets/02cefb60-6b81-40b4-90ce-b51ae974c055" />

The figure above shows two types of subnets:
- Subnets with `/16`, which means that the subnet mask can be written as `255.255.0.0`. This subnet can accommodate around `65,000` hosts.
- Subnets with `/24`, which indicates that the subnet mask can be expressed as `255.255.255.0`. This subnet can have around `250` hosts.

You might want to refer to Task 2 in the Intro to LAN room if you need to learn more about subnetting.

As part of active reconnaissance, we want to discover more information about a group of hosts or about a subnet. If you are on the same subnet, you would expect your scanner to use ARP Address Resolution Protocol (ARP) queries to discover live hosts. An ARP query aims to obtain the hardware address (MAC address) so that communication at the link layer is possible; however, it can also indicate that the host is online. 

If you are in Network A, you can use ARP only to discover the devices within that subnet (`10.1.100.0/24`). Suppose you are connected to a subnet different from the subnet of the target system(s). When your scanner scans devices on another subnet, its packets go through the default gateway (router) to reach them. However, ARP requests cannot pass through the router because ARP only works within the same local network (subnet).

In simple words:
- **IP packets**: Can travel through routers to reach other networks.
- **ARP requests**: Can only work within the local network and cannot cross routers.

---

### Answer the questions below

1. Send a packet with the following:

<img width="195" height="382" alt="image" src="https://github.com/user-attachments/assets/92c11919-c095-4750-9ee7-32e898c5b748" />

- From computer1
- To computer1 (to indicate it is broadcast)
- Packet Type: “ARP Request”
- Data: computer6 (because we are asking for computer6's MAC address using ARP Request)

How many devices can see the ARP Request?

```
4
```

2. Did computer6 receive the ARP Request? (yea/nay)

```
nay
```

3. Send a packet with the following:

<img width="197" height="379" alt="image" src="https://github.com/user-attachments/assets/a925aca5-6ed3-4e35-87e9-f8933a29b421" />

- From computer4
- To computer4 (to indicate it is broadcast)
- Packet Type: “ARP Request”
- Data: computer6 (because we are asking for computer6's MAC address using ARP Request)

How many devices can see the ARP Request?

```
4
```

4. Did computer6 reply to the ARP Request? (yea/nay)

```
yea
```

## Understanding Hosts Discovery through TCP/IP Layer

Starting from bottom to top, we can use:
- ARP from Link Layer
- ICMP from the Network Layer
- TCP from the Transport Layer
- UDP from the Transport Layer

<img width="1200" height="800" alt="image" src="https://github.com/user-attachments/assets/19b8d76c-586b-4dd3-9ee8-1db2250f90b8" />

ARP has one purpose: sending a frame to the broadcast address on the network segment and asking the computer with a specific IP address to respond by providing its MAC (hardware) address.

ICMP has many [types](https://www.iana.org/assignments/icmp-parameters). ICMP ping uses Type 8 (Echo) and Type 0 (Echo Reply).

If you want to ping a system on the same subnet, an ARP query should precede (come before) the ICMP Echo.

Although TCP and UDP are transport-layer protocols, for network scanning, a scanner can send a specially crafted packet to common TCP or UDP ports to check whether the target responds. This method is efficient, especially when ICMP Echo is blocked.

---

### Answer the questions below

1. Send a packet with the following:
- From computer1
- To computer3
- Packet Type: “Ping Request”

What type of packet did computer1 send before the ping?

```
ARP Request
```

<img width="388" height="248" alt="image" src="https://github.com/user-attachments/assets/f734c296-d47d-42f1-b902-98d5fee58d95" />

2. What type of packet did computer1 receive before it was able to send the ping?

```
ARP Response
```

3. How many computers responded to the ping request?

```
1
```

4. Send a packet with the following:
- From computer2
- To computer5
- Packet Type: “Ping Request”

What is the name of the first device that responded to the first ARP Request?

```
Router
```

<img width="383" height="272" alt="image" src="https://github.com/user-attachments/assets/bd85bfba-e567-4f92-997b-a1f6ab60b518" />

5. What is the name of the first device that responded to the second ARP Request?

```
computer5
```

<img width="398" height="273" alt="image" src="https://github.com/user-attachments/assets/c4764b4e-623e-4c64-a1b5-19bbb7bac166" />

6. Send another Ping Request. Did it require new ARP Requests? (yea/nay)

```
nay
```

## Enumerating Targets

Before we explain each in detail and test it against a live target, we need to specify the targets we want to scan. Generally speaking, you can provide a list, a range, or a subnet. 

Examples of target specification are:
- **list**: `MACHINE_IP scanme.nmap.org example.com` will scan 3 IP addresses.
- **range**: `10.11.12.15-20` will scan 6 IP addresses: `10.11.12.15`, `10.11.12.16`,… and `10.11.12.20`. A range can appear in any octet, and Nmap combines them: `10.11.12-13.1-3` scans `2 x 3 = 6` addresses, `.1` to `.3` in both `10.11.12` and `10.11.13`.
- **subnet**: `MACHINE_IP/30` will scan 4 IP addresses.

You can also provide a file as input for your list of targets, `nmap -iL list_of_hosts.txt`.

If you want to check the list of hosts that Nmap will scan, you can use nmap `-sL TARGETS`. This option gives you a detailed list of hosts that Nmap will scan without actually scanning them; however, Nmap will attempt reverse-DNS resolution on all targets to obtain their names. Names might reveal various information to the pentester. (If you don’t want Nmap to use the DNS server, you can add `-n`.)

---

### Connecting to the Network

In this room, you will work with a small network consisting of one Windows host and one Ubuntu host to practice identifying live systems on a network.

When you open the room, you will see a network diagram showing the available hosts. To begin, click the `Start button` to deploy the network. Allow up to 2 minutes for all machines to initialise properly. Once the network has finished loading, launch the `AttackBox` by clicking the Start AttackBox button. When the AttackBox opens in split view, open a Terminal and run Nmap to perform host discovery, then answer the questions in this room.

<img width="254" height="344" alt="image" src="https://github.com/user-attachments/assets/1da42f47-6f6a-4011-9a9d-991df946f15d" />

The questions in this task need only a terminal with Nmap, because `nmap -sL -n` lists targets without sending any packets to them.

---

### Answer the questions below

1. What is the first IP address Nmap would scan if you provided 10.10.12.13/29 as your target?

```
10.10.12.8
```

With command: `nmap -sL -n 10.10.12.13/29`

<img width="515" height="239" alt="image" src="https://github.com/user-attachments/assets/f1ebe988-7209-4669-b529-639780976c59" />

2. How many IP addresses will Nmap scan if you provide the following range: `10.10.0-255.101-125`?

```
6400
```

Command: `nmap -sL -n 10.10.0-255.101-125`

<img width="509" height="251" alt="image" src="https://github.com/user-attachments/assets/899e036c-4d09-4a4d-8c2f-f31f9db19acd" />

## Nmap Host Discovery Using ARP

How would you know which hosts are up and running? It is essential to avoid wasting our time port-scanning an offline host or an IP address not in use. 

There are various ways to discover online hosts. When no host discovery options are provided, Nmap follows the following approaches to discover live hosts:

1. When a privileged user tries to scan targets on a local network (Ethernet), Nmap uses ARP requests. A privileged user is `root` or a user who belongs to `sudoers` and can run `sudo`.
2. When a privileged user tries to scan targets outside the local network, Nmap uses ICMP echo requests, TCP ACK (Acknowledge) to port 80, TCP SYN (Synchronise) to port 443, and ICMP timestamp requests.
3. When an unprivileged user tries to scan targets outside the local network, Nmap resorts to a TCP 3-way handshake by sending SYN packets to ports 80 and 443.

Nmap, by default, uses a ping scan to find live hosts, then proceeds to scan live hosts only. If you want to use Nmap to discover online hosts without port-scanning the live systems, you can issue `nmap -sn TARGETS`. 

Why not run `nmap TARGETS` and let the default probes decide? The defaults suit a typical network, but they can miss a live host. A host firewall may drop ICMP echo requests, and a perimeter firewall may let only a few TCP ports through. When Nmap decides a host is down, it skips that host's port scan, so the host never appears in your results. Choosing the probes yourself, based on what the network lets through, is how you avoid that blind spot.

ARP scan is possible only if you are on the same subnet as the target systems. On an Ethernet (802.3) and Wi-Fi (802.11), you need to know the MAC address of any system before you can communicate with it. The MAC address is required for the link-layer header; it contains the source and destination MAC addresses, among other fields. To get the MAC address, the OS sends an ARP query. A host that replies to ARP queries is up. The ARP query only works if the target is on the same subnet as you, i.e., on the same Ethernet/Wi-Fi network. You should expect to see many ARP queries generated during a Nmap scan of a local network. If you want Nmap only to perform an ARP scan without port-scanning, you can use `nmap -PR -sn TARGETS`, where `-PR` indicates that you only want an ARP scan.

ARP only reaches systems on our own subnet, so we scan the subnet the AttackBox sits on, without any port scanning. We run `nmap -PR -sn 10.49.175.15/24`; the room fills in the IP address of the machine you are connecting from. The target network from Task 4 (`10.200.6.0/24` in our examples) sits on a different subnet, so ARP can't reach it

<img width="629" height="242" alt="image" src="https://github.com/user-attachments/assets/f2609a04-a09f-4895-a47a-b12aed27475c" />

In this case, the AttackBox used ARP requests to discover live hosts on the same subnet. ARP scan works, as shown in the figure below. Nmap sends ARP requests to all target computers, and those that are online should reply with an ARP reply.

<img width="1200" height="596" alt="image" src="https://github.com/user-attachments/assets/5cb3e87d-efc8-4b5c-b202-ffab3b53eac8" />

If we observe the packets generated by tools such as tcpdump or Wireshark, we will notice traffic similar to what is shown in the figure below. In this example, Wireshark displays the source and destination MAC addresses, the protocol, and the ARP query for each request.

<img width="957" height="579" alt="image" src="https://github.com/user-attachments/assets/cc1e28b7-d037-42d1-af36-e1b87db34ed0" />

The source MAC address belongs to the AttackBox, while the destination MAC address is the broadcast address. This is expected, as the target host's MAC address is not yet known. However, the target IP address being queried is visible in the Info column. As shown in the figure, ARP requests are sent sequentially to each IP address on the subnet, starting from `10.201.24.1`.

When a host with the queried IP address is online, it responds with an ARP reply containing its MAC address. Receiving this reply confirms that the host is active and reachable on the network.

ARP scanning is particularly useful during post‑exploitation and internal network enumeration. Once an attacker gains access to a system within a network, ARP scans can be used to quickly and reliably identify other live hosts on the same local segment. Because ARP operates at Layer 2 and is often not filtered by firewalls, it is an effective tool for red-team operations and internal penetration testing.

---

### Answer the questions below

How many hosts are found alive after scanning the 10.49.175.15/24?

```
1
```

Command: `nmap -PR -sn 10.49.175.15/24` but it says 3 hosts are up.

<img width="635" height="200" alt="image" src="https://github.com/user-attachments/assets/ed8df4a4-1403-4e88-843c-60a926ed7daa" />

## Nmap Host Discovery Using ICMP

We can ping every IP address on a target network and see who would respond to our ping (ICMP Type 8/Echo) requests with a ping reply (ICMP Type 0). Simple, isn’t it? Although this would be the most straightforward approach, it is not always reliable. Many firewalls block ICMP echo; new versions of MS Windows are configured with a host firewall that blocks ICMP echo requests by default. 

Remember that an ARP query precedes an ICMP request if your target is on the same subnet.

To use ICMP echo requests to discover live hosts, add the option `-PE` option. (Remember to add `-sn` if you don’t want to follow that with a port scan.)

As shown in the following figure, an ICMP echo scan sends an ICMP echo request and expects the target to reply with an ICMP echo reply if it is online.

<img width="1200" height="598" alt="image" src="https://github.com/user-attachments/assets/4bd11c39-df16-41cf-9eab-b51fce23f7c8" />

---

### Practical

Using the AB, we will scan the target's subnet using `nmap -PE -sn 10.200.6.0/24`. This scan will send ICMP echo packets to every IP address on the subnet. Again, we expect live hosts to reply; however, it is wise to keep in mind that many firewalls block ICMP. 

The output below shows the result of scanning the lab machine’s class C subnet using `sudo nmap -PE -sn 10.200.6.0/24` from the AttackBox.

```
root@ip-10-201-66-6:~# sudo nmap -PE -sn 10.200.6.0/24
sudo: unable to resolve host ip-10-201-66-6: Name or service not known
Starting Nmap 7.80 ( https://nmap.org ) at 2026-02-05 11:51 GMT
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 10.200.6.1
Host is up (0.069s latency).
Nmap scan report for 10.200.6.50
Host is up (0.070s latency).
Nmap scan report for 10.200.6.250
Host is up (0.069s latency).
Nmap done: 256 IP addresses (3 hosts up) scanned in 3.38 seconds
```


















