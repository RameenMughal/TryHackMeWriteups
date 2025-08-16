# Networking Services

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













