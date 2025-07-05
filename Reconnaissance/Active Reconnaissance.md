# Active Reconnaissance

## Introduction

Active reconnaissance requires you to make some kind of contact with your target. This contact can be a phone call or a visit to the target company under some pretence to gather more information, usually as part of social engineering. Alternatively, it can be a direct connection to the target system, whether visiting their website or checking if their firewall has an SSH port open.

Social Engineering: The manipulation of individuals to divulge sensitive information, through various forms of communication

Active reconnaissance begins with direct connections made to the target machine. Any such connection might leave information in the logs showing the client IP address, time of the connection, and duration of the connection, among other things.

## Web Browser

On the transport level, the browser connects to:
- TCP port 80 by default when the website is accessed over HTTP
- TCP port 443 by default when the website is accessed over HTTPS

Since 80 and 443 are default ports for HTTP and HTTPS, the web browser does not show them in the address bar. However, it is possible to use custom ports to access a service.

For instance, `https://127.0.0.1:8834/` will connect to `127.0.0.1` (localhost) at port 8834 via HTTPS protocol. 

While browsing a web page, you can press `Ctrl+Shift+I` on a PC or `Option + Command + I` to open the Developer Tools on Firefox.

Developer Tools lets you inspect many things that your browser has received and exchanged with the remote server. For instance, you can view and even modify the JavaScript (JS) files, inspect the cookies set on your system and discover the folder structure of the site content.

There are also plenty of add-ons for Firefox and Chrome that can help in penetration testing. Here are a few examples:
- **FoxyProxy** lets you quickly change the proxy server you are using to access the target website. This browser extension is convenient when you are using a tool such as Burp Suite or if you need to switch proxy servers regularly.
- **User-Agent Switcher and Manager** gives you the ability to pretend to be accessing the webpage from a different operating system or different web browser. In other words, you can pretend to be browsing a site using an iPhone when in fact, you are accessing it from Mozilla Firefox.
- **Wappalyzer** provides insights about the technologies used on the visited websites. Such extension is handy, primarily when you collect all this information while browsing the website like any other user.

### Answer the questions below

Browse to the following website and ensure that you have opened your Developer Tools on AttackBox Firefox, or the browser on your computer. Using the Developer Tools, figure out the total number of questions.

In the script.js we can see the questions as list with curly brackets 

There are total 8 questions 

![image](https://github.com/user-attachments/assets/c589405c-a2c1-4928-816c-0f81fe23553c)

## Ping
The primary purpose of ping is to check whether you can reach the remote system and that the remote system can reach you back. 

In other words, initially, this was used to check network connectivity; however, we are more interested in its different uses: checking whether the remote system is online.

In simple terms, the ping command sends a packet to a remote system, and the remote system replies. This way, you can conclude that the remote system is online and that the network is working between the two systems.

The ping is a command that sends an ICMP Echo packet to a remote system. If the remote system is online, and the ping packet was correctly routed and not blocked by any firewall, the remote system should send back an ICMP Echo Reply. Similarly, the ping reply should reach the first system if appropriately routed and not blocked by any firewall.

ICMP: Internet Control Message Protocol

The objective of such a command is to ensure that the target system is online before we spend time carrying out more detailed scans to discover the running operating system and services.

You can start to use ping as `ping MACHINE_IP` or `ping HOSTNAME`. In the latter, the system needs to resolve `HOSTNAME` to an IP address before sending the ping packet.

You might consider `ping -c 10 MACHINE_IP` if you just want to send ten packets. This is equivalent to `ping -n 10 MACHINE_IP` on a MS Windows system.

Ping falls under the protocol ICMP (Internet Control Message Protocol). ICMP supports many types of queries, but, in particular, we are interested in ping (ICMP echo/type 8) and ping reply (ICMP echo reply/type 0)

### Answer the questions below

1. Which option would you use to set the size of the data carried by the ICMP echo request?

`-s`

2. What is the size of the ICMP header in bytes?

8

3. Does MS Windows Firewall block ping by default? (Y/N)

Y

4. Deploy the VM for this task and using the AttackBox terminal, issue the command ping -c 10 MACHINE_IP. How many ping replies did you get back?

10

`ping -c 10 10.10.111.208`

## Traceroute

The `traceroute` command traces the route taken by the packets from your system to another host. 

The purpose of a traceroute is to find the IP addresses of the routers or hops that a packet traverses as it goes from your system to a target host. 

This command also reveals the number of routers between the two systems. It is helpful as it indicates the number of hops (routers) between your system and the target host. 

However, note that the route taken by the packets might change as many routers use dynamic routing protocols that adapt to network changes.

`traceroute` tries to discover the routers across the path from your system to the target system.

There is no direct way to discover the path from your system to a target system. We rely on ICMP to “trick” the routers into revealing their IP addresses. 

We can accomplish this by using a small Time To Live (TTL) in the IP header field. Although the T in TTL stands for time, TTL indicates the maximum number of routers/hops that a packet can pass through before being dropped; 

TTL is not a maximum number of time units. When a router receives a packet, it decrements the TTL by one before passing it to the next router. 

If the TTL reaches 0, it will be dropped, and an ICMP Time-to-Live exceeded would be sent to the original sender.

On Linux, `traceroute` will start by sending UDP datagrams within IP packets of TTL being 1. Thus, it causes the first router to encounter a TTL=0 and send an ICMP Time-to-Live exceeded back. Hence, a TTL of 1 will reveal the IP address of the first router to you. Then it will send another packet with TTL=2; this packet will be dropped at the second router. And so on.

`traceroute` sends 3 packets per TTL by default.

To summarize, we can notice the following:
- The number of hops/routers between your system and the target system depends on the time you are running traceroute. There is no guarantee that your packets will always follow the same route, even if you are on the same network or you repeat the traceroute command within a short time.
- Some routers return a public IP address. You might examine a few of these routers based on the scope of the intended penetration testing.
- Some routers don’t return a reply.

### Answer the questions below

1. In Traceroute A, what is the IP address of the last router/hop before reaching tryhackme.com?

`172.67.69.208`

2. In Traceroute B, what is the IP address of the last router/hop before reaching tryhackme.com?

`104.26.11.229`

3. In Traceroute B, how many routers are between the two systems?

26

4. Start the attached VM from Task 3 if it is not already started. On the AttackBox, run traceroute 10.10.111.208. Check how many routers/hops are there between the AttackBox and the target VM.

`traceroute 10.10.111.208`

## Telnet

The TELNET (Teletype Network) protocol was developed in 1969 to communicate with a remote system via a command-line interface (CLI). 

Hence, the command telnet uses the TELNET protocol for remote administration. The default port used by telnet is 23.

From a security perspective, telnet sends all the data, including usernames and passwords, in cleartext. Sending in cleartext makes it easy for anyone, who has access to the communication channel, to steal the login credentials. 

The secure alternative is SSH (Secure SHell) protocol.

Knowing that telnet client relies on the TCP protocol, you can use Telnet to connect to any service and grab its banner. Using `telnet MACHINE_IP PORT`, you can connect to any service running on TCP and even exchange a few messages unless it uses encryption.

### Answer the questions below

1. Start the attached VM from Task 3 if it is not already started. On the AttackBox, open the terminal and use the telnet client to connect to the VM on port 80. What is the name of the running server?

By the telnet command, I am not receiving any information as it instantly closes the connection.

Using curl command `curl -v http://10.10.135.15`

**Answer**: Apache

2. What is the version of the running server (on port 80 of the VM)?

2.4.61

## Netcat

Netcat or simply `nc` has different applications that can be of great value to a pentester. 

Netcat supports both TCP and UDP protocols.

It can function as a client that connects to a listening port; alternatively, it can act as a server that listens on a port of your choice.

First, you can connect to a server, as you did with Telnet, to collect its banner using `nc MACHINE_IP PORT`, which is quite similar to our previous `telnet MACHINE_IP PORT`. Note that you might need to press SHIFT+ENTER after the GET line.

On the server system, where you want to open a port and listen on it, you can issue `nc -lp 1234` or better yet, `nc -vnlp 1234`, which is equivalent to `nc -v -l -n -p 1234`

The exact order of the letters does not matter as long as the port number is preceded directly by `-p`.

Following are options with their meaning:

1.	`-l`: Listen mode

2.	`-p`: Specify the Port number

3.	`-n`: Numeric only; no resolution of hostnames via DNS

4.	`-v`: Verbose output (Detailed Information)

5.	`-vv`: Very Verbose

6.	`-k`: Keep listening after client disconnects

Notes:
- the option -p should appear just before the port number you want to listen on.
- the option -n will avoid DNS lookups and warnings.
- port numbers less than 1024 require root privileges to listen on.

On the client-side, you would issue `nc MACHINE_IP PORT_NUMBER`

Consider the following example. On the server-side, we will listen on port 1234. We can achieve this with the command `nc -vnlp 1234` (same as `nc -lvnp 1234`). In our case, the listening server has the IP address MACHINE_IP, so we can connect to it from the client-side by executing `nc MACHINE_IP 1234`. This setup would echo whatever you type on one side to the other side of the TCP tunnel.

### Answer the questions below

Start the VM and open the AttackBox. Once the AttackBox loads, use Netcat to connect to the VM port 21. What is the version of the running server?

`nc 10.10.6.237 21`

There is FTP Server with version 0.17
