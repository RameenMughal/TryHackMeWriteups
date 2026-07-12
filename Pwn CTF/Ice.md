# Ice

Room: [Ice](https://tryhackme.com/room/ice)

Room Prerequisite: [Nmap](https://tryhackme.com/room/furthernmap)

<img width="935" height="206" alt="image" src="https://github.com/user-attachments/assets/3d944a7e-dee2-43cd-bc1d-48fb376c5b83" />

## Connect

Connect to the TryHackMe network! Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up.

You can check how to connect through the [OpenVPN](https://tryhackme.com/room/openvpn) room.

Write the command: `sudo openvpn <filename>`

## Recon

### Answer the questions below

1. Deploy the machine! This may take up to three minutes to start.

Start the Lab Machine.

2. Launch a scan against our lab machine, I recommend using a SYN scan set to scan all ports on the machine.

Command to scan all the ports with SYN Scan: `nmap -sS -p- TARGET_IP`

Performs a TCP SYN (half-open) scan without completing the TCP three-way handshake. It's faster than a full TCP connect scan.
