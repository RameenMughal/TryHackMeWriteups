# Blue

Room: [Blue](https://tryhackme.com/room/blue)

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




