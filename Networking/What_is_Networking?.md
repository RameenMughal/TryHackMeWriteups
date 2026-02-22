# What is Networking ?

Room: [What is Networking?](https://tryhackme.com/room/whatisnetworking)

<img width="950" height="249" alt="image" src="https://github.com/user-attachments/assets/42b0decc-6a46-4cd8-9204-7aa7af94148e" />

## What is Networking ?

Networks are simply things connected. 

In computing, a network can be formed by anywhere from 2 devices to billions. These devices include everything from your laptop and phone to security cameras, traffic lights and even farming!

Networks are integrated into our everyday life. Be it gathering data for the weather, delivering electricity to homes or even determining who has the right of way at a road. Because networks are so embedded in the modern-day, networking is an essential concept to grasp in cybersecurity.

### Answer the questions below

What is the key term for devices that are connected together?

Network

## What is the Internet ?

The Internet is one giant network that consists of many, many small networks within itself.

The first iteration of the Internet was within the ARPANET (Advanced Research Projects Agency Network) project in the late 1960s. This project was funded by the United States Defence Department and was the first documented network in action. 

However, it wasn't until 1989 when the Internet as we know it was invented by Tim Berners-Lee by the creation of the World Wide Web (WWW). 

The Internet looks like a much larger version of this sort of diagram:

<img width="852" height="579" alt="image" src="https://github.com/user-attachments/assets/95b1917f-3a8a-453f-a7a1-1bcac9c76392" />

As previously stated, the Internet is made up of many small networks all joined together.  These small networks are called private networks, where networks connecting these small networks are called public networks or the Internet! 

So, to recap, a network can be one of two types:
- A private network
- A public network

### Answer the questions below

Who invented the World Wide Web?

Tim Berners-Lee

## Identifying Devices on a Network

To communicate and maintain order, devices must be both identifying and identifiable on a network.

Devices have two means of identification, with one can be changed throughout the network. These are:
1. An IP Address
2. A Media Access Control (MAC) Address - think of this as being similar to a serial number.

### IP Addresses

An IP address (or Internet Protocol) address can be used as a way of identifying a host on a network for a period of time, where that IP address can then be associated with another device without the IP address changing. 

First, let's split up precisely what an IP address is in the diagram below:

<img width="1140" height="487" alt="image" src="https://github.com/user-attachments/assets/923fdc19-9bf3-4b91-9118-fe5d92a4453b" />

An IP address is a set of numbers that are divided into four octets. The value of each octet will summarise to be the IP address of the device on the network. This number is calculated through a technique known as IP addressing & subnetting. IP addresses can change from device to device but cannot be active simultaneously more than once within the same network.

IP Addresses follow a set of standards known as protocols. These protocols are the backbone of networking and force many devices to communicate in the same language. 

However, we should recall that devices can be on both a private and public network. Depending on where they are will determine what type of IP address they have: a public or private IP address.

A public address is used to identify the device on the Internet, whereas a private address is used to identify a device amongst other devices. Public IP addresses are given by your Internet Service Provider (or ISP) at a monthly fee (your bill!)

Enter IP address versions. So far, we have only discussed one version of the Internet Protocol addressing scheme known as IPv4, which uses a numbering system of 2^32 IP addresses (4.29 billion), still short number for many billions of devices.

IPv6 is a new iteration of the Internet Protocol addressing scheme to help tackle this issue. Although it is seemingly more daunting, it boasts a few benefits:
- Supports up to 2^128 of IP addresses (340 trillion-plus), resolving the issues faced with IPv4
- More efficient due to new methodologies

The screenshot below compares both an IPv6 and IPv4 address.

<img width="736" height="177" alt="image" src="https://github.com/user-attachments/assets/fd16b403-599f-4968-824f-b8eafc13094e" />

### MAC Addresses

Devices on a network will all have a physical network interface, which is a microchip board found on the device's motherboard. This network interface is assigned a unique address at the factory it was built at, called a MAC (Media Access Control ) address. 

The MAC address is a twelve-character hexadecimal number (a base sixteen numbering system used in computing to represent numbers) split into two's and separated by a colon. These colons are considered separators. For example, a4:c3:f0:85:ac:2d. 

The first six characters represent the company that made the network interface, and the last six is a unique number.

<img width="1140" height="669" alt="image" src="https://github.com/user-attachments/assets/8861f4fa-8720-46b7-9aee-dba9bb22201a" />

However, an interesting thing with MAC addresses is that they can be faked or "spoofed" in a process known as spoofing. This spoofing occurs when a networked device pretends to identify as another using its MAC address. When this occurs, it can often break poorly implemented security designs that assume that devices talking on a network are trustworthy. 

Take the following scenario: A firewall is configured to allow any communication going to and from the MAC address of the administrator. If a device were to pretend or "spoof" this MAC address, the firewall would now think that it is receiving communication from the administrator when it isn't.

Places such as cafes, coffee shops, and hotels alike often use MAC address control when using their "Guest "or "Public" Wi-Fi. This configuration could offer better services, i.e. a faster connection for a price if you are willing to pay the fee per device.

### Answer the questions below

1. What does the term "IP" stand for?

Internet Protocol

2. What is each section of an IP address called?

Octet

3. How many sections (in digits) does an IPv4 address have? 

4

4. What does the term "MAC" stand for?

Media Access Control

5. Deploy the interactive lab using the "View Site" button and spoof your MAC address to access the site.  What is the flag?

Write the MAC Address of Bob same as Aice to get the flag.

<img width="889" height="795" alt="image" src="https://github.com/user-attachments/assets/14236f88-2f7a-484b-9074-112a0f53c716" />

## Ping (ICMP)

Ping is one of the most fundamental network tools available to us. Ping uses ICMP (Internet Control Message Protocol) packets to determine the performance of a connection between devices, for example, if the connection exists or is reliable.

The time taken for ICMP packets travelling between devices is measured by ping. This measuring is done using ICMP's echo packet and then ICMP's echo reply from the target device.

Pings can be performed against devices on a network, such as your home network or resources like websites. 

This tool can be easily used and comes installed on Operating Systems (OSs) such as Linux and Windows. The syntax to do a simple ping is ping IP address or website URL









