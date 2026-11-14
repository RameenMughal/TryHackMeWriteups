<img width="383" height="272" alt="image" src="https://github.com/user-attachments/assets/fd90063e-5302-41ab-a746-9b00a98f0c03" /># Nmap Live Host Discovery

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

## Nmap Host Discovery using ARP














