# Retro

Room: [Retro](https://tryhackme.com/room/retro)

<img width="940" height="198" alt="image" src="https://github.com/user-attachments/assets/69f16f09-939e-45b3-aff7-80dbfd824869" />

## Pwn

I am using Kali Linux as Attacker Machine and connecting to the TryHackMe server by OpenVPN.

You can see how to connect through OpenVPN by checking the OpenVPN room in TryHackMe.

Command: `sudo openvpn <FILENAME>`

Can you time travel? If not, you might want to think about the next best thing.

Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up.

---

### Answer the questions below

1. A web server is running on the target. What is the hidden directory which the website lives on?

`/retro`

Doing the nmap scan adding the `-Pn` flag as it will not respond to ICMP packets: `nmap -Pn <MACHINE-IP>`

<img width="464" height="144" alt="image" src="https://github.com/user-attachments/assets/dcaaa4d1-fa3e-4cf5-8cd1-f3294dc32aac" />

There is a HTTP Server running at port 80.

Checking the link `http://<MACHINE-IP>/`, we see IIS Windows Server

<img width="1100" height="439" alt="image" src="https://github.com/user-attachments/assets/bc6f7ff7-becf-4efc-8587-908a3579660b" />

Then we just guessed that if the challenge name is Retro then there will be directory named `retro` I guess.

Link: `http://<MACHINE_IP>/retro/`

<img width="1120" height="440" alt="image" src="https://github.com/user-attachments/assets/e4b74799-9a7b-4ae1-bc26-509116d788b2" />

You can also check the `retro` directory by `gobuster` command: `gobuster dir -u http://MACHINE_IP/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt`

<img width="717" height="237" alt="image" src="https://github.com/user-attachments/assets/40d7b972-c3dd-4b3e-ab19-5cc65ab2fb3d" />

2. user.txt

By checking the `retro` page we see that it is from Wade name Retro Fanatics.

As our motive will be to collect information to get credentials of login.

Scrolling down we see second last post which he says about forgetting the avatar name when he logs in, so the goal is to find the avatar name.

<img width="763" height="356" alt="image" src="https://github.com/user-attachments/assets/b137f193-d3d2-4a2e-870e-b97cd2774f16" />

Clicking the "Wade" link goes to the Wade Profile `http://TARGET_IP/retro/index.php/author/wade/` about his posts and comments, so we can see that he has commented on the same post "Ready Player One" where he mentioned about logging in and forgetting the avatar name.




