# Blaster

Room: [Blaster](https://tryhackme.com/room/blaster)

<img width="941" height="206" alt="image" src="https://github.com/user-attachments/assets/94944600-8cab-45af-b015-7e3279e8221a" />

## Mission Start!

Throughout this room, we'll be looking at alternative modes of exploitation without the use of Metasploit or really exploitation tools in general beyond nmap and dirbuster.

To wrap up the room, we'll be pivoting back to these tools for persistence and additional steps we can take.

*This room is a remix of my previous room [Retro](https://tryhackme.com/room/retro) with some complications I added to that room having been removed. For increased difficulty and an exercise in patience, check that room out after this. In addition, this room is the sequel to [Ice](https://tryhackme.com/room/ice). - DarkStar747*

Start the Lab Machine and connect to the TryHackMe Server by OpenVPN: `sudo openvpn FILENAME`.

You can check how to connect through OpenVPN by this room: [OpenVPN](https://tryhackme.com/room/openvpn)

## Activate Forward Scanners and Launch Proton Torpedoes

Run nmap scan: `nmap -Pn TARGET_IP`

<img width="328" height="106" alt="image" src="https://github.com/user-attachments/assets/b02e7843-2ae2-4520-8bfd-06d1960ba1ca" />

**Note**: `-Pn` because to not ping it as it has Windows Firewall enabled so without this flag it will not respond, it will say that the host seems down.

### Answer the questions below

1. How many ports are open on our target system?

2

2. Looks like there's a web server running, what is the title of the page we discover when browsing to it?

IIS Windows Server

<img width="760" height="352" alt="image" src="https://github.com/user-attachments/assets/e27f30e7-afcf-4751-a304-1916e5fc6631" />

3. Interesting, let's see if there's anything else on this web server by fuzzing it. What hidden directory do we discover?

`/retro`

First I tried the gobsuter command with common wordlist that did not show any result: `gobuster dir -u http://TARGET_IP/ -w /usr/share/wordlists/dirb/common.txt`

Then seeing the hint, now using the small wordlist: `gobuster dir -u http://TARGET_IP/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt`

<img width="545" height="175" alt="image" src="https://github.com/user-attachments/assets/93b43f92-4009-40a2-9790-fe7b5e47f366" />

4. Navigate to our discovered hidden directory, what potential username do we discover?

Wade

<img width="764" height="398" alt="image" src="https://github.com/user-attachments/assets/b002c3d2-b90f-4239-b745-211639974699" />

5. Crawling through the posts, it seems like our user has had some difficulties logging in recently. What possible password do we discover?

parzival

First scrolling down we see second last post which he says about forgetting the avatar name when he logs in, so the goal is to find the avatar name.

<img width="565" height="254" alt="image" src="https://github.com/user-attachments/assets/00469e06-5272-4c45-82df-773a01058aee" />

Clicking the "Wade" link goes to the Wade Profile `http://TARGET_IP/retro/index.php/author/wade/` about his posts and comments, so we can see that he has commented on the same post "Ready Player One" where he mentioned about logging in and forgetting the avatar name.

<img width="574" height="293" alt="image" src="https://github.com/user-attachments/assets/b1cda2d3-8391-40b3-9e83-2207df9c941c" />

Opening this link `http://TARGET_IP/retro/index.php/2019/12/09/ready-player-one/#comment-2` shows us the comment indicating the avatar name:

<img width="578" height="195" alt="image" src="https://github.com/user-attachments/assets/1e9029b3-1236-4569-9b56-c10fd23532fb" />

6. Log into the machine via Microsoft Remote Desktop (MSRDP) and read user.txt. What are it's contents?

Command: `xfreerdp /v:TARGET_IP /u:Wade /p:'parzival'` and open the user.txt file

<img width="1239" height="358" alt="image" src="https://github.com/user-attachments/assets/0b7cab07-00ad-4a3a-b61d-fd4d71c22088" />

## Breaching the Control Room

### Answer the questions below

1. When enumerating a machine, it's often useful to look at what the user was last doing. Look around the machine and see if you can find the CVE which was researched on this server. What CVE was it?

CVE-2019-1388

I could not find the CVE in the Windows even watching the official walkthrough so I found out that other people are also having this issue that they cannot see the CVE in Internet Explorere History. So I got to know from the Hint and checking the walkthrough.

Original way is to open the Internet Explorer, click the Start icon and you see the CVE under History of 2 weeks ago but in mine I dont see that.

<img width="505" height="225" alt="image" src="https://github.com/user-attachments/assets/0d256d37-7d38-45bd-a9c7-5ebfa1561a39" />

You can also check there is an application named `hhupd` so you can search about it in Google and you will get to know about this CVE.

2. Looks like an executable file is necessary for exploitation of this vulnerability and the user didn't really clean up very well after testing it. What is the name of this executable?

`hhupd`

<img width="390" height="152" alt="image" src="https://github.com/user-attachments/assets/875cf387-b175-4192-bf3d-b6a7f61bb735" />

3. Research vulnerability and how to exploit it. Exploit it now to gain an elevated terminal!

CVE-2019-1388 is a Windows User Account Control (UAC) bypass vulnerability. It lets a normal user gain Administrator (SYSTEM-level) privileges without knowing the administrator password.

When Windows wants to verify a program, it shows a certificate.

That certificate has a "View Certificate" button.

Microsoft forgot to properly restrict what users could do from that certificate window.

An attacker can abuse it to open Internet Explorer with administrator privileges.

From Internet Explorer, they can:
1. Open File → Open
2. Browse to C:\Windows\System32
3. Run cmd.exe

Since Internet Explorer is already running as Administrator, Command Prompt also opens as Administrator.

Now the attacker has full control of the computer.

You can check about this vulnerability on this website [NIST CVE-2019-1388 Detail](https://nvd.nist.gov/vuln/detail/cve-2019-1388)

Now for exploiting this machine, Open hhupd exe and click "Show More Details".

<img width="249" height="257" alt="image" src="https://github.com/user-attachments/assets/225056ee-abb3-4ec5-9227-49a40e696075" />

Click on show about the publishers certificate.

<img width="238" height="275" alt="image" src="https://github.com/user-attachments/assets/42f2e160-0171-46d6-ae87-f2d33cfd959d" />

Click on the CA Issued by "VeriSign Commercial Software Publishers CA"

<img width="244" height="281" alt="image" src="https://github.com/user-attachments/assets/8e265049-1dae-4bdc-965a-f0a11ffbc506" />

A browser page will open up.

<img width="510" height="203" alt="image" src="https://github.com/user-attachments/assets/a6f0ea96-5c4d-40d2-bbe3-cc6392eb939d" />

Click the Settings Gear icon and select "File" and then "Save as", then a dialog box will appear indicating that a file is not available.

<img width="511" height="233" alt="image" src="https://github.com/user-attachments/assets/1fe974f3-e7ff-4a77-93a9-5194b0169bda" />

Then save the Filename as `c:\Windows\system32\*.*` and press Save so we can open this directly indirectly.

<img width="514" height="250" alt="image" src="https://github.com/user-attachments/assets/c7b86e57-4616-4d83-b56d-10259ac9f500" />

Now search "cmd" at the upper right space indicating Search icon, scroll down to get the cmd.

<img width="512" height="237" alt="image" src="https://github.com/user-attachments/assets/1fe86ad0-83af-486f-a0c2-ad5487e335ae" />

Open the cmd and you have gained Administrator rights.

<img width="511" height="257" alt="image" src="https://github.com/user-attachments/assets/20d2080b-7387-4002-a305-42da4e7885e2" />

4. Now that we've spawned a terminal, let's go ahead and run the command 'whoami'. What is the output of running this?

<img width="229" height="74" alt="image" src="https://github.com/user-attachments/assets/5291cebe-63b8-4af1-b816-5fe252a29140" />

5. Now that we've confirmed that we have an elevated prompt, read the contents of root.txt on the Administrator's desktop. What are the contents? Keep your terminal up after exploitation so we can use it in task four!

Go to the directory by command `cd c:\Users\Administrator\Desktop` and then see the contents by command `type root.txt`

<img width="489" height="234" alt="image" src="https://github.com/user-attachments/assets/e0bf4d7a-1971-4a90-80a3-1d1c818bacd4" />







































