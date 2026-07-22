# Enumeration & Brute Force

Room: [Enumeration & Brute Force](https://tryhackme.com/room/enumerationbruteforce)

Pre-requisites:
1. [Burp Suite Module](https://tryhackme.com/module/learn-burp-suite)
2. [Linux Fundamentals Module](https://tryhackme.com/module/linux-fundamentals)

<img width="937" height="206" alt="image" src="https://github.com/user-attachments/assets/81e0d097-eeb4-4784-9748-21e6e7b6217e" />

## Introduction

Authentication enumeration is a fundamental aspect of security testing, concentrating specifically on the mechanisms that protect sensitive aspects of web applications; this process involves methodically inspecting various authentication components ranging from username validation to password policies and session management. Each of these elements is meticulously tested because they represent potential vulnerabilities that, if exploited, could lead to significant security breaches.

---

### Pre-requisites

Before starting this room, you should have a basic understanding of the following concepts:
- Familiarity with HTTP and HTTPS, including request/response structures and common status codes.
- Experience using tools like Burp Suite.
- Basic proficiency in navigating and using the Linux command line.

---

### Answer the questions below

Deploy the target VM attached to this task by pressing the green Start Lab Machine button. After obtaining the machine's generated IP address, you can either use the AttackBox or your own VM connected to TryHackMe's VPN.

I am using my Kali Linux Machine, so you can check [OpenVPN](https://tryhackme.com/room/openvpn) room to connect to the TryHackMe Server. Connect by command: `sudo openvpn FILENAME`

Add `TARGET_IP` to your `/etc/hosts` file. For example:

```
TARGET_IP    enum.thm
```

Write command `sudo nano /etc/hosts` to open the file and then copy paste `TARGET_IP` and `enum.thm` there.

<img width="270" height="80" alt="image" src="https://github.com/user-attachments/assets/21fcf890-05b0-4fb1-a4bd-78cde0769803" />

After 3 minutes, visit `http://enum.thm` to access the machine.

