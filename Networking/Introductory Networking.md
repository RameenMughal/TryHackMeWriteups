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

