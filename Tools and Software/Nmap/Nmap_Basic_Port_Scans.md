# Nmap Basic Port Scans

Room: [Nmap Basic Port Scans](https://tryhackme.com/room/nmap02)

Prerequisites:
1. [Nmap Live Host Discovery](https://tryhackme.com/room/nmap01)
2. [Network Services](https://tryhackme.com/room/networkservices)
3. [Network Security Essentials](https://tryhackme.com/room/networksecurityessentials)

<img width="950" height="211" alt="image" src="https://github.com/user-attachments/assets/580c6538-fd56-4292-8e43-6f52ac316e62" />

## Introduction 

### Learning Objectives

The next step would be to check which ports are open and listening, and which are closed. Therefore, in this room and the next one, we focus on port scanning and the different types of port scans used by `nmap`. This room explains:
- TCP connect port scan
- TCP SYN port scan
- UDP port scan

Moreover, we discuss the options for specifying ports, the scan rate, and the number of parallel probes.

---

### Connecting to the Machine

Please click the `Start Machine` button to boot up the VM and I am using Kali Linux Machine as AttackBox.

Connecting my machine to TryHackMe Server by OpenVPN command: `sudo openvpn <FILENAME>`

## TCP and UDP Ports

In the same way that an IP address specifies a host on a network among many others, a TCP or UDP port identifies a network service running on that host. A server provides a network service and adheres to a specific network protocol. Examples include providing time, responding to DNS queries, and serving web pages. A port is usually linked to a service using that specific port number. For instance, an HTTP server would bind to TCP port 80 by default; if it supports SSL/TLS, it would also listen on TCP port 443. (TCP ports 80 and 443 are the default ports for HTTP and HTTPS; however, the web server administrator might choose other port numbers if necessary.) Furthermore, no more than one service can listen on any TCP or UDP port (on the same IP address).

At the risk of oversimplification, we can classify ports into two states:
- An open port indicates that a service is listening on that port.
- A closed port indicates that no service is listening on that port.

However, in practical situations, we need to consider the impact of firewalls. For instance, a port might be open, but a firewall might be blocking the packets. Therefore, Nmap considers the following six states:

1. An **open** port indicates that a service is listening on the specified port.
2. A **closed** port indicates that no service is listening on the specified port, although the port is accessible. By accessible, we mean that it is reachable and is not blocked by a firewall or other security appliances/programs.
3. **Filtered** means that Nmap cannot determine whether the port is open or closed because it is not accessible. This state is usually due to a firewall preventing Nmap from reaching that port. Nmap’s packets may be blocked from reaching the port; alternatively, responses may be blocked from reaching Nmap’s host.
4. **Unfiltered** means that Nmap cannot determine whether the port is open or closed, even though the port is accessible. This state is encountered when using an ACK scan `-sA`.
5. **Open|Filtered**: This means that Nmap cannot determine whether the port is open or filtered.
6. **Closed|Filtered**: This means that Nmap cannot decide whether a port is closed or filtered.

---

### Answer the questions below

1. Which service uses UDP port 53 by default?

```
DNS
```

2. Which service uses TCP port 22 by default?

```
SSH
```

3. How many port states does Nmap consider?

```
6
```

4. Which port state is the most interesting to discover as a pentester?

```
open
```

## TCP Flags

Nmap supports different types of TCP port scans. To understand the difference between these port scans, we need to review the TCP header. The TCP header is the first 24 bytes of a TCP segment. The following figure shows the TCP header as defined in [RFC 793](https://datatracker.ietf.org/doc/html/rfc793.html). 

This figure looks sophisticated at first; however, it is pretty simple to understand. In the first row, we have the source TCP port and the destination TCP port. We can see that the port number is allocated 16 bits (2 bytes). In the second and third rows, we have the sequence number and the acknowledgement number. Each row has 32 bits (4 bytes) allocated, for a total of 6 rows, making 24 bytes.

<img width="2400" height="1480" alt="image" src="https://github.com/user-attachments/assets/3302873e-5688-40fc-8078-ec2dcac7c5bf" />

In particular, we need to focus on the flags that Nmap can set or unset. We have highlighted the TCP flags in red. Setting a flag bit means setting its value to 1. From left to right, the TCP header flags are:

1. `URG`: Urgent flag indicates that the urgent pointer field is significant. The urgent pointer indicates that the incoming data is urgent, and that a TCP segment with the URG flag set is processed immediately, without waiting for previously sent TCP segments.
2. `ACK`: Acknowledgement flag indicates that the acknowledgement number is significant. It is used to acknowledge the receipt of a TCP segment.
3. `PSH`: Push flag asking TCP to pass the data to the application promptly.
4. `RST`: The reset flag is used to reset the connection. Another device, such as a firewall, might send it to tear a TCP connection. This flag is also used when data is sent to a host, and there is no service on the receiving end to answer.
5. `SYN`: The synchronise flag is used to initiate a TCP 3-way handshake and synchronise sequence numbers with the other host. The sequence number should be set randomly during TCP connection establishment.
6. `FIN`: The sender has no more data to send.

---

### Answer the questions below

1. What 3 letters represent the Reset flag?

```
RST
```

2. Which flag needs to be set when you initiate a TCP connection (first packet of TCP 3-way handshake)?

```
SYN
```







