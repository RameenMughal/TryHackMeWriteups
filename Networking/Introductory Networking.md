# Introductory Networking

## The OSI Model: An Overview

The OSI (Open Systems Interconnection) Model is a standardised model which we use to demonstrate the theory behind computer networking. In practice, it's actually the more compact TCP/IP model that real-world networking is based off; however the OSI model, in many ways, is easier to get an initial understanding from.

The OSI model consists of seven layers:

<img width="134" height="279" alt="image" src="https://github.com/user-attachments/assets/43dcc628-07ee-4cb6-b231-f313ca26c3f9" />

### Layer 7 - Application:

The application layer of the OSI model essentially provides networking options to programs running on a computer. It works almost exclusively with applications, providing an interface for them to use in order to transmit data. 

When data is given to the application layer, it is passed down into the presentation layer.

### Layer 6 - Presentation:

The presentation layer receives data from the application layer. This data tends to be in a format that the application understands, but it's not necessarily in a standardised format that could be understood by the application layer in the receiving computer. 

The presentation layer translates the data into a standardised format, as well as handling any encryption, compression or other transformations to the data. With this complete, the data is passed down to the session layer.

### Layer 5 - Session:

When the session layer receives the correctly formatted data from the presentation layer, it looks to see if it can set up a connection with the other computer across the network. If it can't then it sends back an error and the process goes no further. 

If a session can be established then it's the job of the session layer to maintain it, as well as co-operate with the session layer of the remote computer in order to synchronise communications. 

The session layer is particularly important as the session that it creates is unique to the communication in question. This is what allows you to make multiple requests to different endpoints simultaneously without all the data getting mixed up (think about opening two tabs in a web browser at the same time)! 

When the session layer has successfully logged a connection between the host and remote computer the data is passed down to Layer 4: the transport Layer.

### Layer 4 - Transport:

The transport layer is a very interesting layer that serves numerous important functions. Its first purpose is to choose the protocol over which the data is to be transmitted. 

The two most common protocols in the transport layer are **TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)**; with TCP the transmission is connection-based which means that a connection between the computers is established and maintained for the duration of the request. This allows for a reliable transmission, as the connection can be used to ensure that the packets all get to the right place. A TCP connection allows the two computers to remain in constant communication to ensure that the data is sent at an acceptable speed, and that any lost data is re-sent. With UDP, the opposite is true; packets of data are essentially thrown at the receiving computer -- if it can't keep up then that's its problem (this is why a video transmission over something like Skype can be pixelated if the connection is bad). 

What this means is that TCP would usually be chosen for situations where accuracy is favoured over speed (e.g. file transfer, or loading a webpage), and UDP would be used in situations where speed is more important (e.g. video streaming).

With a protocol selected, the transport layer then divides the transmission up into bite-sized pieces (over TCP these are called segments, over UDP they're called datagrams), which makes it easier to transmit the message successfully. 

### Layer 3 - Network:

The network layer is responsible for locating the destination of your request. For example, the Internet is a huge network; when you want to request information from a webpage, it's the network layer that takes the IP address for the page and figures out the best route to take. 

At this stage we're working with what is referred to as Logical addressing (i.e. IP addresses) which are still software controlled. Logical addresses are used to provide order to networks, categorising them and allowing us to properly sort them. 

Currently the most common form of logical addressing is the IPV4 format, which you'll likely already be familiar with (i.e 192.168.1.1 is a common address for a home router).

### Layer 2 - Data Link:

The data link layer focuses on the physical addressing of the transmission. It receives a packet from the network layer (that includes the IP address for the remote computer) and adds in the physical (MAC) address of the receiving endpoint. 

Inside every network enabled computer is a Network Interface Card (NIC) which comes with a unique MAC (Media Access Control) address to identify it.

MAC addresses are set by the manufacturer and literally burnt into the card; they can't be changed - although they can be spoofed (imitate  a MAC address for attack) . When information is sent across a network, it's actually the physical address that is used to identify where exactly to send the information.

Additionally, it's also the job of the data link layer to present the data in a format suitable for transmission.

The data link layer also serves an important function when it receives data, as it checks the received information to make sure that it hasn't been corrupted during transmission, which could well happen when the data is transmitted by layer 1: the physical layer.

### Layer 1 - Physical:

The physical layer is right down to the hardware of the computer. This is where the electrical pulses that make up data transfer over a network are sent and received. 

It's the job of the physical layer to convert the binary data of the transmission into signals and transmit them across the network, as well as receiving incoming signals and converting them back into binary data.

### Answer the questions below

1. Which layer would choose to send data over TCP or UDP? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

4

2. Which layer checks received information to make sure that it hasn't been corrupted? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

2

3. In which layer would data be formatted in preparation for transmission? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

2

4. Which layer transmits and receives data? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

1

5. Which layer encrypts, compresses, or otherwise transforms the initial data to give it a standardised format? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

6

6. Which layer tracks communications between the host and receiving computers? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

5

7. Which layer accepts communication requests from applications? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

7

8. Which layer handles logical addressing? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

3

9. When sending data over TCP, what would you call the "bite-sized" pieces of data? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

Segments

10. [Research] Which layer would the FTP protocol communicate with? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

7

11. Which transport layer protocol would be best suited to transmit a live video? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

UDP

## Encapsulation

As the data is passed down each layer of the model, more information containing details specific to the layer in question is added on to the start of the transmission.

As an example, the header added by the Network Layer would include things like the source and destination IP addresses, and the header added by the Transport Layer would include (amongst other things) information specific to the protocol being used. 

The data link layer also adds a piece on at the end of the transmission, which is used to verify that the data has not been corrupted on transmission; this also has the added bonus of increased security, as the data can't be intercepted and tampered with without breaking the trailer. 

At the Data Link Layer, when data is prepared for transmission, a trailer is added at the end — usually something like a Frame Check Sequence (FCS) or CRC (Cyclic Redundancy Check).

If someone tried to intercept the frame and change even a single bit of the payload, the CRC/FCS in the trailer would no longer match, and the receiver would detect the alteration and reject the frame.

This whole process is referred to as encapsulation; the process by which data can be sent from one computer to another.

<img width="1718" height="822" alt="image" src="https://github.com/user-attachments/assets/81d88ece-abfe-46ca-b9e5-519caac09100" />

Notice that the encapsulated data is given a different name at different steps of the process. 

In layers 7,6 and 5, the data is simply referred to as data. 

In the transport layer the encapsulated data is referred to as a segment or a datagram (depending on whether TCP or UDP has been selected as a transmission protocol). 

At the Network Layer, the data is referred to as a packet. When the packet gets passed down to the Data Link layer it becomes a frame, and by the time it's transmitted across a network the frame has been broken down into bits.

When the message is received by the second computer, it reverses the process - starting at the physical layer and working up until it reaches the application layer, stripping off the added information as it goes. This is referred to as de-encapsulation.

### Answer the questions below

1. How would you refer to data at layer 2 of the encapsulation process (with the OSI model)?

Frames

2. How would you refer to data at layer 4 of the encapsulation process (with the OSI model), if the UDP protocol has been selected?

Datagrams

3. What process would a computer perform on a received message?

De-Encapsulation

4. Which is the only layer of the OSI model to add a trailer during encapsulation?

Data Link

5. Does encapsulation provide an extra layer of security (Aye/Nay)?

Aye

## The TCP/IP Model

The TCP/IP model is, in many ways, very similar to the OSI model. It's a few years older, and serves as the basis for real-world networking. 

The TCP/IP model consists of four layers: Application, Transport, Internet and Network Interface. Between them, these cover the same range of functions as the seven layers of the OSI Model.

<img width="153" height="176" alt="image" src="https://github.com/user-attachments/assets/94137c7e-0100-435c-b196-1327a9089417" />

**Note**: Some recent sources split the TCP/IP model into five layers - breaking the Network Interface layer into Data Link and Physical layers (as with the OSI model). This is accepted and well-known; however, it is not officially defined (unlike the original four layers which are defined in RFC1122). It's up to you which version you use - both are generally considered valid.

The two models match up something like this:

<img width="259" height="279" alt="image" src="https://github.com/user-attachments/assets/8ec1c917-481f-4226-b0b2-aa720d42992b" />

The processes of encapsulation and de-encapsulation work in exactly the same way with the TCP/IP model as they do with the OSI model. At each layer of the TCP/IP model a header is added during encapsulation, and removed during de-encapsulation.

TCP/IP takes its name from the two most important of these: the Transmission Control Protocol (which we touched upon earlier in the OSI model) that controls the flow of data between two endpoints, and the Internet Protocol, which controls how packets are addressed and sent. 

TCP is a connection-based protocol. In other words, before you send any data via TCP, you must first form a stable connection between the two computers. The process of forming this connection is called the three-way handshake

When you attempt to make a connection, your computer first sends a special request to the remote server indicating that it wants to initialise a connection. This request contains something called a SYN (short for synchronise) bit, which essentially makes first contact in starting the connection process. The server will then respond with a packet containing the SYN bit, as well as another "acknowledgement" bit, called ACK. Finally, your computer will send a packet that contains the ACK bit by itself, confirming that the connection has been setup successfully. With the three-way handshake successfully completed, data can be reliably transmitted between the two computers. Any data that is lost or corrupted on transmission is re-sent, thus leading to a connection which appears to be lossless.

<img width="613" height="439" alt="image" src="https://github.com/user-attachments/assets/4c5e29a5-50e2-4069-872d-340c47029a8d" />

**History**: To begin with there was no standardisation - different manufacturers followed their own methodologies, and consequently systems made by different manufacturers were completely incompatible when it came to networking. The TCP/IP model was introduced by the American DoD (Department of Defense) in 1982 to provide a standard. This sorted out the inconsistency problems. Later the OSI model was also introduced by the International Organisation for Standardisation (ISO); however, it's mainly used as a more comprehensive guide for learning, as the TCP/IP model is still the standard upon which modern networking is based.

### Answer the questions below

1. Which model was introduced first, OSI or TCP/IP?

TCP/IP

2. Which layer of the TCP/IP model covers the functionality of the Transport layer of the OSI model (Full Name)?

Transport

3. Which layer of the TCP/IP model covers the functionality of the Session layer of the OSI model (Full Name)?

Application

4. The Network Interface layer of the TCP/IP model covers the functionality of two layers in the OSI model. These layers are Data Link, and?.. (Full Name)?

Physical

5. Which layer of the TCP/IP model handles the functionality of the OSI network layer?

Internet

6. What kind of protocol is TCP?

Connection-based

7. What is SYN short for?

Synchronise

8. What is the second step of the three way handshake?

SYN/ACK

9. What is the short name for the "Acknowledgement" segment in the three-way handshake?

ACK

## Ping

The `ping` command is used when we want to test whether a connection to a remote resource is possible. Usually this will be a website on the internet, but it could also be for a computer on your home network if you want to check if it's configured correctly. 

Ping works using the ICMP (nternet Control Message Protocol), which is one of the slightly less well-known TCP/IP protocols that were mentioned earlier. The ICMP protocol works on the Network layer of the OSI Model, and thus the Internet layer of the TCP/IP model. 

The basic syntax for ping is `ping <target>`

<img width="423" height="99" alt="image" src="https://github.com/user-attachments/assets/6ac51070-3135-4f30-9691-a3b164fcb413" />

Notice that the `ping` command actually returned the IP address for the Google server that it connected to, rather than the URL that was requested. This is a handy secondary application for ping, as it can be used to determine the IP address of the server hosting a website.

### Answer the questions below

1. What command would you use to ping the bbc.co.uk website?

`ping bbc.co.uk`

2. Ping muirlandoracle.co.uk, What is the IPv4 address?

Command `ping muirlandoracle.co.uk` to get the IPv4 address

`217.160.0.152`

3. What switch lets you change the interval of sent ping requests?

`-i`

4. What switch would allow you to restrict requests to IPv4?

`-4`

5. What switch would give you a more verbose output?

`-v`

## Traceroute

Traceroute can be used to map the path your request takes as it heads to the target machine.

The internet is made up of many, many different servers and end-points, all networked up to each other. This means that, in order to get to the content you actually want, you first need to go through a bunch of other servers. Traceroute allows you to see each of these connections - it allows you to see every intermediate step between your computer and the resource that you requested. 

The basic syntax for traceroute on Linux is this: `traceroute <destination>`

By default, the Windows `tracert` command finds the path to a destination by sending ICMP Echo Request packets, similar to how `ping` works. On the other hand, the Unix/Linux `traceroute` command normally uses UDP packets to high, unused port numbers. 

In both cases, routers along the path reply when the packet’s TTL runs out, allowing the tool to list each hop. You can change the default protocol in either tool by using special command switches, such as making Unix `traceroute` use ICMP or TCP instead of UDP.

### Answer the questions below

1. What switch would you use to specify an interface when using Traceroute?

`-i`

2. What switch would you use if you wanted to use TCP SYN requests when tracing the route?

`-T`

3. [Lateral Thinking] Which layer of the TCP/IP model will traceroute run on by default (Windows)?

Internet

## WHOIS

Domain Names - the unsung saviours of the internet.

A domain translates into an IP address so that we don't need to remember it (e.g. you can type tryhackme.com, rather than the TryHackMe IP address). 

Domains are leased out by companies called Domain Registrars. If you want a domain, you go and register with a registrar, then lease the domain for a certain length of time.

Whois essentially allows you to query who a domain name is registered to.

Whois lookups are very easy to perform. Just use `whois <domain>` to get a list of available information about the domain registration

### Answer the questions below

1. What is the registrant postal code for facebook.com?

94025

2. When was the facebook.com domain first registered (Format: DD/MM/YYYY)?

29/03/1997

3. Which city is the registrant based in?

Redmond

4. [OSINT] What is the name of the golf course that is near the registrant address for microsoft.com?

The Registrant Street is One Microsoft Way, so I searched in the Google Maps "Golf course One Microsoft Way". Got some results, tried each name and got the right one.

Bellevue Golf Course

5. What is the registered Tech Email for microsoft.com?

msnhst@microsoft.com

## Dig

Ever wondered how a URL gets converted into an IP address that your computer can understand? The answer is a TCP/IP protocol called DNS (Domain Name System).

At the most basic level, DNS allows us to ask a special server to give us the IP address of the website we're trying to access. 

For example, if we made a request to www.google.com, our computer would first send a request to a special DNS server (which your computer already knows how to find). The server would then go looking for the IP address for Google and send it back to us. Our computer could then send the request to the IP of the Google server.

You make a request to a website. The first thing that your computer does is check its local "Hosts File" to see if an explicit IP->Domain mapping has been created. This is an older system than DNS and much less commonly used in modern environments; however, it still takes precedence in the search order of most operating systems. 

If no mapping has been manually created, the computer then checks its local DNS cache to see if it already has an IP address stored for the website; if it does, great. If not, it goes to the next stage of the process.

Assuming the address hasn't already been found, your computer will then send a request to what is known as a recursive DNS server. These will automatically be known to the router on your network. Many Internet Service Providers (ISPs) maintain their own recursive servers, but companies such as Google and OpenDNS also control recursive servers. This is how your computer automatically knows where to send the request for information: details for a recursive DNS server are stored in your router or computer. 

This server will also maintain a cache of results for popular domains; however, if the website you've requested isn't stored in the cache, the recursive server will pass the request on to a root name server.

Before 2004 there were precisely 13 root name DNS servers in the world. These days there are many more; however, they are still accessible using the same 13 IP addresses assigned to the original servers (balanced so that you get the closest server when you make a request). 

The root name servers essentially keep track of the DNS servers in the next level down, choosing an appropriate one to redirect your request to. These lower level servers are called Top-Level Domain servers.

Top-Level Domain (TLD) servers are split up into extensions. 

So, for example, if you were searching for tryhackme.com your request would be redirected to a TLD server that handled .com domains. If you were searching for bbc.co.uk your request would be redirected to a TLD server that handles .co.uk domains. 

As with root name servers, TLD servers keep track of the next level down: Authoritative name servers. When a TLD server receives your request for information, the server passes it down to an appropriate Authoritative name server.

Authoritative name servers are used to store DNS records for domains directly. 

In other words, every domain in the world will have its DNS records stored on an Authoritative name server somewhere or another; they are the source of the information. When your request reaches the authoritative name server for the domain you're querying, it will send the relevant information back to you, allowing your computer to connect to the IP address behind the domain you requested.

When you visit a website in your web browser this all happens automatically, but we can also do it manually with a tool called `dig` . Like `ping` and `traceroute`, `dig` should be installed automatically on Linux systems.

Dig allows us to manually query recursive DNS servers of our choice for information about domains: `dig <domain> @<dns-server-ip>`

<img width="319" height="181" alt="image" src="https://github.com/user-attachments/assets/07076af6-10cd-45f4-8125-5b1dbab99fa5" />

In summary, that information is telling us that we sent it one query and successfully (i.e. No Errors) received one full answer -- which, as expected, contains the IP address for the domain name that we queried.

Another interesting piece of information that dig gives us is the TTL (Time To Live) of the queried DNS record. As mentioned previously, when your computer queries a domain name, it stores the results in its local cache. The TTL of the record tells your computer when to stop considering the record as being valid -- i.e. when it should request the data again, rather than relying on the cached copy.

This means that when your computer looks up a website’s IP address, it saves that information for a certain amount of time — called the TTL (Time To Live).

The TTL can be found in the second column of the answer section

It's important to remember that TTL (in the context of DNS caching) is measured in seconds

### Answer the questions below

1. What is DNS short for?

Domain Name System

2. What is the first type of DNS server your computer would query when you search for a domain?

Recursive

3. What type of DNS server contains records specific to domain extensions (i.e. .com, .co.uk*, etc)*? Use the long version of the name.

Top-Level Domain

4. Where is the very first place your computer would look to find the IP address of a domain?

Hosts File

5. [Research] Google runs two public DNS servers. One of them can be queried with the IP `8.8.8.8`, what is the IP address of the other one?

`8.8.4.4`

6. If a DNS query has a TTL of 24 hours, what number would the dig query show?

86400

