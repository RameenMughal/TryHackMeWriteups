# Retro

Room: [Retro](https://tryhackme.com/room/retro)

This challenge is similar to the [Blaster](https://tryhackme.com/room/blaster)

You can see the challenge writeup also in Penetration Testing directory.

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

By checking the `retro` page we see that it is from Wade named Retro Fanatics.

As our motive will be to collect information to get credentials of login.

Scrolling down we see second last post which he says about forgetting the avatar name when he logs in, so the goal is to find the avatar name.

<img width="763" height="356" alt="image" src="https://github.com/user-attachments/assets/b137f193-d3d2-4a2e-870e-b97cd2774f16" />

Clicking the "Wade" link goes to the Wade Profile `http://TARGET_IP/retro/index.php/author/wade/` about his posts and comments, so we can see that he has commented on the same post "Ready Player One" where he mentioned about logging in and forgetting the avatar name.

<img width="770" height="399" alt="image" src="https://github.com/user-attachments/assets/103ee571-d658-474f-a1b3-11273b12a733" />

Clicking the Recent Comment Link `http://TARGET_IP/retro/index.php/2019/12/09/ready-player-one/#comment-2` shows us the comment indicating the avatar name:

<img width="779" height="259" alt="image" src="https://github.com/user-attachments/assets/d0e6798e-278e-4407-86a4-e9bb4c4de2dc" />

So we know that the password is `parzival` and username is `Wade`

We can try to log in without the password by Microsoft Remote Desktop software as it will be Microsoft Operating System.

Command: `xfreerdp /v:TARGET_IP /u:Wade /p:'parzival'` and open the `user.txt` file

<img width="779" height="253" alt="image" src="https://github.com/user-attachments/assets/99818d14-3ca6-46c5-910a-6c1f22cd9f33" />

3. root.txt

You see the Google Chrome, we can check that to see any clues, we see in Bookmarks tab, there is a [CVE-2019-1388](https://nvd.nist.gov/vuln/detail/cve-2019-1388):

<img width="684" height="117" alt="image" src="https://github.com/user-attachments/assets/0b5b0a82-e248-4638-ab82-62814c04687d" />

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

We can see the `hhupd.exe` file in the Recycle bin which is used for the for the popup to view the certificate. Restore the file.

<img width="645" height="364" alt="image" src="https://github.com/user-attachments/assets/ac5ec56c-99b5-461e-ada2-eb96010e625e" />

What `hhupd.exe` is: `hhupd.ex`e is a legacy Microsoft HTML Help update/installer executable.

The connection: `hhupd.exe` was historically involved in a known UAC privilege escalation vulnerability (tracked as CVE-2019-1388), where running an older signed executable like `hhupd.exe` as an administrator allowed an attacker to interact with the UAC certificate dialog box to spawn a browser or command prompt with `NT AUTHORITY\SYSTEM `privileges. However, hhupd.exe itself is just a file, not the UAC system.

Now for exploiting this machine, Open `hhupd.exe` and click "Show More Details".

<img width="321" height="343" alt="image" src="https://github.com/user-attachments/assets/c2fe83a6-ad0f-44f1-8032-827c40d48834" />

<img width="318" height="364" alt="image" src="https://github.com/user-attachments/assets/270cf679-4f2b-4907-b1bc-8b16cc25e877" />

Click on show about the publishers certificate.

<img width="320" height="373" alt="image" src="https://github.com/user-attachments/assets/033b6f91-183e-451e-bdf3-ebf69df87f3b" />

Click on the CA Issued by "VeriSign Commercial Software Publishers CA", A browser page will open up, I am selecting Internet Explorer.

<img width="675" height="289" alt="image" src="https://github.com/user-attachments/assets/5bdad035-e8cd-4b3e-aeff-4500fb90b45e" />

Click the Settings Gear icon and select "File" and then "Save as", then a dialog box will appear indicating that a file is not available.

<img width="669" height="346" alt="image" src="https://github.com/user-attachments/assets/d2f9c7ee-137e-4128-9e36-5b47307de206" />

Notice the `c:\Windows\system32\` that it runs as the Administrator already, close the dialog box.

Then save the Filename as `c:\Windows\system32\*.*` and press Save so we can open this directory indirectly.

<img width="549" height="350" alt="image" src="https://github.com/user-attachments/assets/10c14521-695a-4872-a769-ca43135c4688" />

Now search "cmd" at the upper right space indicating Search icon, scroll down to get the cmd.

<img width="620" height="354" alt="image" src="https://github.com/user-attachments/assets/6eb7a815-c61e-4365-ada6-745d776f2fc8" />

Open the cmd and you have gained Administrator rights.

<img width="574" height="331" alt="image" src="https://github.com/user-attachments/assets/9c176fbc-fe28-4376-a59f-9175c8e55f49" />

Go to the directory by command `cd c:\Users\Administrator\Desktop` and then see the contents by command `type root.txt`

<img width="328" height="138" alt="image" src="https://github.com/user-attachments/assets/c9971677-cd47-4628-9e6c-deeefcf3032b" />

<img width="301" height="50" alt="image" src="https://github.com/user-attachments/assets/4b87d36e-deee-405e-981a-f4e73ccd35d3" />






















