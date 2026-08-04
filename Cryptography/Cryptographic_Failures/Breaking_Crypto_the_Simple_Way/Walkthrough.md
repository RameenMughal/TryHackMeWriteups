# Breaking Crypto the Simple Way

Room: [Breaking Crypto the Simple Way](https://tryhackme.com/room/breakingcryptothesimpleway)

Prerequisites:
1. [Cryptography Module](https://tryhackme.com/module/cryptography)
2. [Cryptography-101 Module](https://tryhackme.com/module/cryptography-101)

<img width="945" height="202" alt="image" src="https://github.com/user-attachments/assets/761da9ec-67cb-4e26-9851-b836e61dd990" />

## Introduction

Cryptography is designed to protect sensitive data, but it's only effective when implemented correctly. Even small mistakes in how cryptographic systems are set up can open the door for attackers. These mistakes are surprisingly common and often become "quick wins" during penetration testing or real-world attacks.

For example, using a weak encryption key or a predictable random number generator can make encryption easier to break. Similarly, exposing secrets like API keys in client-side code gives attackers everything they need to bypass cryptographic protections.

---

### Prerequisites

Before starting this room, you should have a basic understanding of the following concepts:
1. How cryptographic concepts like encryption, decryption, and hashing work.
2. Tools like Hashcat or John the Ripper are used to crack passwords and keys.
3. HTTP request and response basics, along with some experience using the command line.
4. Completion of [Cryptography](https://tryhackme.com/module/cryptography) and [Cryptography-101](https://tryhackme.com/module/cryptography-101) modules.

---

### Starting the Machine

Deploy the target VM attached to this task by pressing the green Start Lab Machine button. After obtaining the machine's generated IP address, you can either use the AttackBox or your own VM connected to TryHackMe's VPN.

I am using my Kali Linux Machine, so we will connect to the TryHackMe through OpenVPN by command: `sudo openvpn FILENAME`

You can check the room [OpenVPN](https://tryhackme.com/room/openvpn) to know how to connect through this.

To add the hostname `bcts.thm`, first open the file by `sudo nano /etc/hosts`

Copy paste the hostname and IP address like this `10.49.129.162 bcts.thm`

<img width="281" height="80" alt="image" src="https://github.com/user-attachments/assets/e29c2789-205e-4aa6-b16d-8661605e8116" />

Save the file and then access the website `http://bcts.thm/`

<img width="611" height="182" alt="image" src="https://github.com/user-attachments/assets/b8a7514a-3822-4ee2-83b7-bfe405e1de5e" />




