# Insecure Randomness

Room: [Insecure Randomness](https://tryhackme.com/room/insecurerandomness)

Prerequisites: [OWASP Top 10 - 2025 Module](https://tryhackme.com/module/owasp-top-10-2025)

<img width="947" height="209" alt="image" src="https://github.com/user-attachments/assets/f4d67f18-970e-43d4-9935-888e6f03bc27" />

## Introduction

Insecure randomness occurs when web applications use predictable or poorly generated random values, making them vulnerable to attacks. While randomness is essential for securing tokens, session IDs, and cryptographic keys, insecure implementation can allow attackers to exploit these predictable values to bypass authentication, hijack sessions, or even decrypt sensitive data.

In this room, we will explore techniques to identify and exploit vulnerabilities caused by insecure randomness. This will provide you with the knowledge to assess and enhance the security of web applications by ensuring proper random number generation practices. 

---

### Connecting to the Machine

You can start the lab machine by clicking the "Start Lab Machine" button attached to this task. You may access the VM using the AttackBox or your VPN connection. 

I will be using my Kali Linux to connect to the TryHackMe Server by command: `sudo openvpn FILENAME`

You can check how to connect through OpenVPN by this room: [OpenVPN](https://tryhackme.com/room/openvpn)

You can access the web app by visiting the URL h`ttp://random.thm:8090/case/` but first, you must add the hostname in your OS or AttackBox.

First open the file to add hostname by `sudo nano /etc/hosts`

Then copy paste the `MACHINE_IP random.thm` into the file.

Save the file and type `http://random.thm:8090/case/` in the browser to access the website.


