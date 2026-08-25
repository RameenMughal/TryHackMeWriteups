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

## Quick Recap

In the last SQL injection room, we explored the basics of SQL injection, understanding how attackers exploit vulnerabilities in web applications to manipulate SQL queries and access unauthorised data. We covered essential techniques, such as error-based and union-based SQL injection, and blind SQL injection methods, such as boolean-based and time-based attacks. 

<img width="708" height="385" alt="image" src="https://github.com/user-attachments/assets/8380ab3d-97dc-4221-a45d-5fd909a3d608" />

---

### In-band SQL Injection

This technique is considered the most common and straightforward type of SQL injection attack. In this technique, the attacker uses the same communication channel for both the injection and the retrieval of data. There are two primary types of in-band SQL injection:
- **Error-Based SQL Injection**: The attacker manipulates the SQL query to produce error messages from the database. These error messages often contain information about the database structure, which can be used to exploit the database further.
  - Example: `SELECT * FROM users WHERE id = 1 AND 1=CONVERT(int, (SELECT @@version))`. If the database version is returned in the error message, it reveals information about the database.
- **Union-Based SQL Injection**: The attacker uses the UNION SQL operator to combine the results of two or more SELECT statements into a single result, thereby retrieving data from other tables.
  - Example: `SELECT name, email FROM users WHERE id = 1 UNION ALL SELECT username, password FROM admin`.

---

### Inferential (Blind) SQL Injection

Inferential SQL injection does not transfer data directly through the web application, making exploiting it more challenging. Instead, the attacker sends payloads and observes the application’s behaviour and response times to infer information about the database. There are two primary types of inferential SQL injection:
- **Boolean-Based Blind SQL Injection**: The attacker sends an SQL query to the database, forcing the application to return a different result based on a true or false condition. By analysing the application’s response, the attacker can infer whether the payload was true or false.
  - Example: `SELECT * FROM users WHERE id = 1 AND 1=1` (true condition) versus `SELECT * FROM users WHERE id = 1 AND 1=2` (false condition). The attacker can infer the result if the page content or behaviour changes based on the condition.
- **Time-Based Blind SQL Injection**: The attacker sends an SQL query to the database, which delays the response for a specified time if the condition is true. By measuring the response time, the attacker can infer whether the condition is true or false.
  - For example, `SELECT * FROM users WHERE id = 1; IF (1=1) WAITFOR DELAY '00:00:05'--`. If the response is delayed by 5 seconds, the attacker can infer that the condition was true.
 
---

### Out-of-band SQL Injection

Out-of-band SQL injection is used when the attacker cannot use the same channel to launch the attack and gather results or when the server responses are unstable. This technique relies on the database server making an out-of-band request (e.g., HTTP or DNS) to send the query result to the attacker. HTTP is normally used in out-of-band SQL injection to send the query result to the attacker's server.

In-band SQL Injection is easy to exploit and detect but noisy and can be easily monitored. Inferential (Blind) SQL Injection is more challenging to exploit and requires multiple requests but can be used when detailed error messages are unavailable. Out-of-band SQL Injection is less common and highly effective, requires external server control, and relies on the database’s ability to make out-of-band requests. 

---

### Answer the questions below

1. What type of SQL injection uses the same communication channel for both the injection and data retrieval?

In-band

2. In out-of-band SQL injection, which protocol is usually used to send query results to the attacker's server?

HTTP

