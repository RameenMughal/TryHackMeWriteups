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

Command to scan all the ports with SYN Scan: `nmap -sS -p- -T4 TARGET_IP`

Performs a TCP SYN (half-open) scan without completing the TCP three-way handshake. It's faster than a full TCP connect scan.

<img width="345" height="218" alt="image" src="https://github.com/user-attachments/assets/60c9716d-7ae4-4038-bb07-6464790e9e16" />

3. Once the scan completes, we'll see a number of interesting ports open on this machine. As you might have guessed, the firewall has been disabled (with the service completely shutdown), leaving very little to protect this machine. One of the more interesting ports that is open is Microsoft Remote Desktop (MSRDP). What port is this open on?

3389

We can see that the firewall must be disabled as we can see ports like RDP (3389), SMB (445) and RPC (135), like on normal Windows Firewall Defender, these are normally blocked or restricted to be accessible by the public.

4. What service did nmap identify as running on port 8000? (First word of this service)

Icecast, by command: `nmap -sC -sV -p8000 TARGET_IP`

<img width="479" height="124" alt="image" src="https://github.com/user-attachments/assets/7fce9c31-89fe-4706-8d7b-65ad2b20515e" />

5. What does Nmap identify as the hostname of the machine? (All caps for the answer)

DARK-PC, by command: `nmap -sC -sV -p- TARGET_IP`

<img width="563" height="326" alt="image" src="https://github.com/user-attachments/assets/b896370b-5807-4bc3-b826-de101e29c172" />

## Gain Access

You can refer to the [Icecast Exploit -Rapid7](https://www.rapid7.com/db/modules/exploit/windows/http/icecast_header/) to know about the vulnerability.

### Answer the questions below

1. Now that we've identified some interesting services running on our lab machine, let's do a little bit of research into one of the weirder services identified: Icecast. Icecast, or well at least this version running on our target, is heavily flawed and has a high level vulnerability with a score of 7.5 (7.4 depending on where you view it). What is the Impact Score for this vulnerability? Use [CVE Details: CVE-2004-1561](https://www.cvedetails.com) for this question and the next.

6.4

<img width="781" height="97" alt="image" src="https://github.com/user-attachments/assets/18ce7b7b-42eb-4f9f-9c2a-cc42c7274ad6" />

2. What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000

CVE-2004-1561



