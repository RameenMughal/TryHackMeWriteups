# Advanced SQL Injection

Room: [Advanced SQL Injection](https://tryhackme.com/room/advancedsqlinjection)

Prerequisites:
1. [SQL Injection](https://tryhackme.com/room/sqlinjectionlm)
2. [SQLMAP](https://tryhackme.com/room/sqlmap)
3. [OWASP Top 10 (2025)](https://tryhackme.com/module/owasp-top-10-2025)
4. [Nmap](https://tryhackme.com/room/furthernmap)

<img width="941" height="203" alt="image" src="https://github.com/user-attachments/assets/90622ad5-eee0-4b6e-9d6d-d698ac816e83" />

## Introduction

SQL injection remains one of web applications' most severe and widespread security vulnerabilities. This threat arises when an attacker exploits a web application's ability to execute arbitrary SQL queries, leading to unauthorised access to the database, data exfiltration, data manipulation, or even complete control over the application. 

---

### Connecting to the Machine

You can start the lab machine by clicking the `Start Lab Machine` button attached to this task. You may access the VM using the AttackBox or your VPN connection.

I am using my Kali Linux machine by connecting through OpenVPN Command: `sudo openvpn FILENAME`

You can refer to how to connect through OpenVPN by this room: [OpenVPN](https://tryhackme.com/room/openvpn)

Before diving in, it's crucial to clearly understand the lab machine's database version and operating system details. To achieve this, we can utilise Nmap, a powerful network scanning tool, to thoroughly scan the `MACHINE_IP`. This scan will provide valuable insights into the open ports, running services, and the lab machine's operating system.

Firstly identifying the open ports in the Machine: `nmap MACHINE_IP`

<img width="340" height="169" alt="image" src="https://github.com/user-attachments/assets/9abc6cbf-94f9-4a53-ab9d-1a8a97009745" />

Now doing aggresive scan: `nmap -A -T4 -p 3306,3389,445,139,135 MACHINE_IP`

```
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-25 12:36 -0400
Nmap scan report for 10.48.164.234
Host is up (0.071s latency).

PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3306/tcp open  mysql         MariaDB 10.3.23 or earlier (unauthorized)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=SQLi
| Not valid before: 2026-08-24T16:32:26
|_Not valid after:  2027-02-23T16:32:26
|_ssl-date: 2026-08-25T16:37:16+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: SQLI
|   NetBIOS_Domain_Name: SQLI
|   NetBIOS_Computer_Name: SQLI
|   DNS_Domain_Name: SQLi
|   DNS_Computer_Name: SQLi
|   Product_Version: 10.0.17763
|_  System_Time: 2026-08-25T16:37:08+00:00
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Microsoft Windows 10 1709 - 22H2 (97%), Microsoft Windows Server 2019 (96%), Microsoft Windows Server 2016 (95%), Microsoft Windows 10 1903 (93%), Microsoft Windows 11 24H2 - 25H2 (93%), Microsoft Windows 10 1803 (92%), Microsoft Windows Server 2012 (92%), Microsoft Windows Server 2022 (92%), Microsoft Windows Vista SP1 (92%), Microsoft Windows 10 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 3 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-08-25T16:37:10
|_  start_date: N/A

TRACEROUTE (using port 3389/tcp)
HOP RTT      ADDRESS
1   53.35 ms 192.168.128.1
2   ...
3   53.92 ms 10.48.164.234

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.68 seconds
```

`-A` means Aggresive Scan which does several advanced Nmap detection features at once:
- OS detection — tries to identify the target's operating system.
- Version detection — determines what software/services and their versions are running.
- Default NSE (Nmap Scripting Engine) scripts — runs Nmap's default scripts to gather additional information.
- Traceroute — attempts to determine the network path to the target.

And then the interesting ports were selected to do further scan on them.

The machine is using MySQL service on Windows.

---

### Answer the questions below

What is the port on which MySQL service is running?

3306



