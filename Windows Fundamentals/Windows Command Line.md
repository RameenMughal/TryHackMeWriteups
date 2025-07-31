# Windows Command Line

## Introduction

You can use the SSH client on the AttackBox to connect to `MACHINE_IP` with the following credentials:

Username: `user`

Password: `Tryhackme123!`

### Answer the questions below

What is the default command line interpreter in the Windows environment?

cmd.exe

## Basic System Information

Before issuing commands, we should note that we can only issue the commands within the Windows Path. You can issue the command `set` to check your path from the command line. 

The terminal output below shows the path where MS Windows will execute commands, as indicated by the line starting with `Path=`.

<img width="404" height="215" alt="image" src="https://github.com/user-attachments/assets/6e2a23de-7e1a-4ab7-ba53-d7227a9f9975" />

Let’s use the `ver` command to determine the operating system (OS) version. 

<img width="215" height="53" alt="image" src="https://github.com/user-attachments/assets/61a86557-83a6-41f1-9cbf-1b02793edd20" />

We can run the systeminfo command to list various information about the system such as OS information, system details, processor and memory.

<img width="315" height="156" alt="image" src="https://github.com/user-attachments/assets/c8379c57-ef3a-4a5d-838e-d0123f547714" />

Before moving on, it is good to mention a couple of tricks.

First, you can pipe it through more if the output is too long. Then, you can view it page after page by pressing the space bar button. 

To demonstrate this, try running `driverquery` and compare it with running `driverquery | more`

In the latter, you can display the output page by page and you can exit it using `CTRL + C`.

### Answer the questions below

1. What is the OS version of the Windows VM?

By using the `ver` command.

**Answer**: 10.0.20348.2655

2. What is the hostname of the Windows VM?

By using the `systeminfo` command, you see Host Name first

**Answer**: WINSRV2022-CORE

## Network Troubleshooting

### Network Configuration

You can check your network information using `ipconfig`. The terminal output below shows our IP address, subnet mask, and default gateway.

<img width="310" height="139" alt="image" src="https://github.com/user-attachments/assets/7975b7da-2b79-4d08-8302-d98af8c406c1" />

You can also use `ipconfig /all` for more information about your network configuration. As shown in the terminal below, we can view our DNS servers and confirm that DHCP is enabled.

<img width="378" height="312" alt="image" src="https://github.com/user-attachments/assets/d90be907-52df-4d15-9fdf-1083994678f5" />

### Network Troubleshooting

One common troubleshooting task is checking if the server can access a particular server on the Internet. The command syntax is `ping target_name`. Inspired by ping-pong, we send a specific ICMP packet and listen for a response. If a response is received, we know that we can reach the target and that the target can reach us.

Another valuable tool for troubleshooting is `tracert`, which stands for trace route. The command `tracert target_name` traces the network route traversed to reach the target. Without getting into more details, it expects the routers on the path to notify us if they drop a packet because its time-to-live (TTL) has reached zero. 

### More Networking Commands

One networking command worth knowing is `nslookup`. It looks up a host or domain and returns its IP address. The syntax `nslookup example.com` will look up `example.com` using the default name server; however, `nslookup example.com 1.1.1.1` will use the name server `one.one.one.one`

<img width="262" height="203" alt="image" src="https://github.com/user-attachments/assets/4d8b80bd-361b-42f2-adc2-853a7dedddeb" />

The final networking command we will cover in this room is `netstat`. This command displays current network connections and listening ports. A basic `netstat` command with no arguments will show you established connections

<img width="320" height="66" alt="image" src="https://github.com/user-attachments/assets/837d1e68-0ec3-408b-bd2f-bf716a189791" />

If you are curious about the other options, you can run `netstat -h`, where `-h` displays the help page. We opted for the following options:
- `-a` - displays all established connections and listening ports
- `-b` - shows the program associated with each listening port and established connection
- `-o` - reveals the process ID (PID) associated with the connection
- `-n` - uses a numerical form for addresses and port numbers

We combine these four options and execute the `netstat -abon` command. The result is quite long, but we display the first few lines in the terminal below. 

It is clear now that the executable `sshd.exe` is responsible for listening for incoming connections on port 22, as shown in the first line. We can also see the process ID (PID) associated with each connection.

<img width="377" height="162" alt="image" src="https://github.com/user-attachments/assets/4cc20934-3ec3-4409-a357-cfdaa6f4ab3c" />

### Answer the questions below

1. Which command can we use to look up the server’s physical address (MAC address)?

`ipconfig/all`

2. What is the name of the process listening on port 3389?

TermService

3. What is the subnet mask?

`255.255.0.0`






