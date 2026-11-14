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






