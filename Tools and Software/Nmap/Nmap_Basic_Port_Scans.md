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

## TCP Connect Scan

TCP connect scan works by completing the TCP 3-way handshake. In standard TCP connection establishment, the client sends a TCP packet with the SYN flag set, and the server responds with SYN/ACK if the port is open; finally, the client completes the 3-way handshake by sending an ACK.

<img width="1200" height="589" alt="image" src="https://github.com/user-attachments/assets/64ec632b-b3b2-455f-b563-f38f4b620f36" />

We are interested in learning whether the TCP port is open, not in establishing a TCP connection. Hence, the connection is torn as soon as its state is confirmed by sending a RST/ACK. You can choose to run a TCP connect scan using -sT.

<img width="1200" height="584" alt="image" src="https://github.com/user-attachments/assets/38e1f510-8a15-4882-9782-20007fbb2cfc" />

It is important to note that if you are not a privileged user (root or sudoer), a TCP connect scan is the only possible option to discover open TCP ports.

In the following Wireshark packet capture window, we see Nmap sending TCP packets with the SYN flag set to various ports, 5900, 22, 80, and so on. By default, Nmap will attempt to connect to the 1000 most common ports. A closed TCP port responds to a SYN packet with RST/ACK to indicate that it is not open. This pattern will repeat for all the closed ports as we attempt to initiate a TCP 3-way handshake with them.

<img width="985" height="575" alt="image" src="https://github.com/user-attachments/assets/4dc6efa8-8f53-44d5-9a2b-6000f06a5a31" />

We notice that port 80 is open, so it replied with a SYN/ACK, and Nmap completed the 3-way handshake by sending an ACK. The figure below shows all the packets exchanged between our Nmap host and the target system’s port 80. The first three packets are the TCP 3-way handshake. Then the fourth packet tears it down with an RST/ACK.

<img width="990" height="210" alt="image" src="https://github.com/user-attachments/assets/e19129d7-ec11-484b-bdc7-5b3420d4ce8f" />

To illustrate the `-sT` (TCP connect scan), Run the following command in the AB to get a detailed list of the open ports.

<img width="457" height="173" alt="image" src="https://github.com/user-attachments/assets/b12cc787-408e-40bf-b7b4-f0cf96ff68c0" />

Note that we can use `-F` to enable fast mode and decrease the number of scanned ports from 1000 to 100 most common ports.

It is worth mentioning that the `-r` option can also be added to scan the ports in consecutive order instead of random order. This option is useful for testing whether ports open consistently, for instance, when a target boots up.

---

### Answer the questions below

1. What is the state of the FTP service running on port 21?

```
open
```

2. What is Nmap’s guess about the service running on port 53?

```
domain
```

## TCP SYN Scan

Unprivileged users are limited to the connect scan. However, the default scan mode is a SYN scan, and it requires a privileged (`root` or `sudo`) user to run. SYN scan does not need to complete the TCP 3-way handshake; instead, it tears down the connection after receiving a response from the server. Because we didn’t establish a TCP connection, the scan is less likely to be logged. We can select this scan type by using the `-sS` option.

The figure below shows how the TCP SYN scan works without completing the TCP 3-way handshake.

<img width="1200" height="583" alt="image" src="https://github.com/user-attachments/assets/5b8e4543-8205-4658-8048-10ddd0ae3e46" />

We see how a SYN scan -sS does not need to complete the TCP 3-way handshake; instead, Nmap sends an RST packet once a SYN/ACK packet is received.

<img width="1056" height="192" alt="image" src="https://github.com/user-attachments/assets/7c6bdf08-7a27-438e-8477-cb8d39f5d6ae" />

TCP SYN scan is the default scan mode when running Nmap as a privileged user (`root` or `sudo`), and it is a very reliable choice. It has successfully discovered the open ports you found earlier with the TCP connect scan, yet no TCP connection was fully established with the target.

<img width="464" height="171" alt="image" src="https://github.com/user-attachments/assets/d9be5f47-5e28-4ebf-a325-6838f853a5c0" />

---

### Answer the questions below

1. After launching a TCP SYN scan, how many SYN-ACK packets are successfully received in AttackBox?

```
4
```

Open Wireshark and select the `tun0` interface and then run the Nmap command `nmap -sS <MACHINE_IP>`

When it runs then see the WireShark you see packets recorded, use the filter `ip.src == <MACHINE_IP> && tcp.flags.syn == 1 && tcp.flags.ack == 1`

<img width="863" height="171" alt="image" src="https://github.com/user-attachments/assets/ac63b4e4-cf72-4705-b14c-1f9eb9ce2073" />

2. How many ports are open on the target machine?

```
4
```

## UDP Scan

UDP is a connectionless protocol; hence, it does not require a handshake for connection establishment. We cannot guarantee that a service listening on a UDP port would respond to our packets. However, if a UDP packet is sent to a closed port, an ICMP port unreachable error (type 3, code 3) is returned. You can select UDP scan using the `-sU` option; moreover, you can combine it with another TCP scan.

The following figure shows that if we send a UDP packet to an open UDP port, we cannot expect a reply. Therefore, sending a UDP packet to an open port won’t tell us anything.

<img width="1200" height="583" alt="image" src="https://github.com/user-attachments/assets/09a12364-001c-42e5-bdfb-2f1a8665a0b2" />

However, as shown in the figure below, we expect to receive an ICMP type 3, code 3, destination unreachable, port unreachable message. In other words, the UDP ports that don’t generate any response are the ones that Nmap will state as open.

<img width="1200" height="636" alt="image" src="https://github.com/user-attachments/assets/563396e0-f02b-423a-bb74-acb1ae6ab869" />

In the Wireshark capture below, we can see that every closed port generates an ICMP destination unreachable (port unreachable) message.

<img width="1034" height="582" alt="image" src="https://github.com/user-attachments/assets/cebbd312-2b40-4dbc-9d83-286d7bfc4819" />

From the AB, use the following command to perform a UDP scan of the top 10 ports on the target machine:

<img width="464" height="257" alt="image" src="https://github.com/user-attachments/assets/3e35c3d0-5026-4c31-93bd-7f2248265985" />

---

### Answer the questions below

1. What is the state of port number 161 over UDP in the target machine?

```
closed
```

2. What is the service name according to Nmap on port 161?

```
snmp
```

## Fine-Tuning and Scope Performance

You can specify the ports you want to scan instead of the default 1000 ports. Specifying the ports is intuitive by now. Let’s see some examples: 
- port list: `-p22,80,443` will scan ports 22, 80 and 443.
- port range: `-p1-1023` will scan all ports between 1 and 1023 inclusive, while -p20-25 will scan ports between 20 and 25 inclusive.

You can request the scan of all ports by using `-p-`, which will scan all 65535 ports. If you want to scan the most common 100 ports, add `-F`. Using `--top-ports 10` will check the ten most common ports.

You can control the scan timing using `-T<0-5>`. `-T0` is the slowest (paranoid), while `-T5` is the fastest. According to the Nmap manual page, there are six templates:
- paranoid (0)
- sneaky (1)
- polite (2)
- normal (3)
- aggressive (4)
- insane (5)

To avoid IDS alerts, you might consider `-T0` or `-T1`. For instance, `-T0` scans one port at a time and waits 5 minutes between sending each probe, so you can guess how long scanning one target would take to finish. If you don’t specify any timing, Nmap uses normal `-T3`. Note that `-T5` is the most aggressive in terms of speed; however, this can affect the accuracy of the scan results due to the increased likelihood of packet loss. Note that `-T4` is often used during CTFs and when learning to scan on practice targets, whereas `-T1` is often used during real engagements where stealth is more important.

Moreover, you can control probing parallelisation using `--min-parallelism <numprobes>` and `--max-parallelism <numprobes>`. Nmap probes targets to discover which hosts are live and which ports are open; the probing parallelisation parameter specifies the number of such probes that can run in parallel. For instance, `--min-parallelism=512` pushes Nmap to maintain at least 512 probes in parallel; these 512 probes are related to host discovery and open ports.

Probes are the packets that Nmap sends to a target system to check whether it is alive or whether its ports are open.

Parallelisation means how many probes Nmap can send or handle at the same time.

---

### Answer the questions below

1. What is the option to scan all the TCP ports between 5000 and 5500?

```
-p5000-5500
```

2. How can you ensure that Nmap will run at least 64 probes in parallel?

```
--min-parallelism=64
```

3. What option would you add to make Nmap very slow and paranoid?

```
-T0
```

## Summary

This room covered three types of scans.

| Port Scan Type       | Example Command          |
|----------------------|--------------------------|
| TCP Connect Scan     | `nmap -sT MACHINE_IP`    |
| TCP SYN Scan         | `sudo nmap -sS MACHINE_IP` |
| UDP Scan             | `sudo nmap -sU MACHINE_IP` |

These scan types should get you started discovering running TCP and UDP services on a target host.

| Option                 | Purpose                                   |
|------------------------|-------------------------------------------|
| `-p-`                  | Scan all ports                            |
| `-p1-1023`              | Scan ports 1 to 1023                      |
| `-F`                   | Scan the 100 most common ports             |
| `-r`                   | Scan ports in consecutive order           |
| `-T<0-5>`              | `-T0` is the slowest and `-T5` is the fastest |
| `--max-rate 50`        | Rate ≤ 50 packets/sec                     |
| `--min-rate 15`        | Rate ≥ 15 packets/sec                     |
| `--min-parallelism 100` | At least 100 probes in parallel           |













