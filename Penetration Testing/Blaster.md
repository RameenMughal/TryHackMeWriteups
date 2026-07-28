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














