# Blue

Room: [Blue](https://tryhackme.com/room/blue)

Rrerequisite Rooms:
1. [Nmap](https://tryhackme.com/room/furthernmap)
2. [Metasploit](https://tryhackme.com/module/metasploit)

<img width="932" height="189" alt="image" src="https://github.com/user-attachments/assets/e935a766-a301-4bec-ac14-56a4ff8c48b3" />

## Recon

Start the Lab Machine and if using your Kali Machine, connect to the TryHackMe server by `sudo openvpn <FILENAME>`

### Answer the questions below

1. Scan the machine.

write `nmap <TARGET_IP>` to scan the target system.

<img width="331" height="167" alt="image" src="https://github.com/user-attachments/assets/94f5bf34-ae1a-416b-9e0b-6fa2d3713a29" />

2. How many ports are open with a port number under 1000?

3 (ports 135, 139 and 445)

4. What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067)

ms17-010

Specifically for the EternalBlue room, you can check the smb vulnerability by: `nmap --script smb-vuln* -p445 <TARGET_IP>`

<img width="521" height="275" alt="image" src="https://github.com/user-attachments/assets/d121ed40-a478-461c-963c-089af62635e6" />

## Gain Access

### Answer the questions below

1. Start Metasploit.

Write command: `msfconsole`

<img width="350" height="335" alt="image" src="https://github.com/user-attachments/assets/679c2023-218f-4c8b-9ed7-e65a508fddcd" />

2. Find the exploitation code we will run against the machine. What is the full path of the code? (Ex: exploit/........)

Write command: `search ms17-010` to find the path of the exploit. The first option 0 is the answer: `exploit/windows/smb/ms17_010_eternalblue`

<img width="848" height="248" alt="image" src="https://github.com/user-attachments/assets/df858c6e-6009-43c6-b635-6f71d57f936a" />

Write command `use 0` to select the desired path.

<img width="598" height="78" alt="image" src="https://github.com/user-attachments/assets/a7f4a546-43aa-47b1-b1b3-110f0d31cf94" />

3. Show options and set the one required value. What is the name of this value? (All caps for submission)

Check the parameters by command: `show options`. RHOSTS is the answer of this question.

<img width="677" height="338" alt="image" src="https://github.com/user-attachments/assets/d7bb1a37-6892-4825-aba6-3e6710520ac0" />











