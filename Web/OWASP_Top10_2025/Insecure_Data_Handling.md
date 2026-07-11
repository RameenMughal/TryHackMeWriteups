# OWASP Top 10 2025: Insecure Data Handling

Room: [OWASP Top 10 2025: Insecure Data Handling](https://tryhackme.com/room/owasptopten2025three)

<img width="933" height="197" alt="image" src="https://github.com/user-attachments/assets/25678e6d-88c6-4ba2-80ca-56c3128bd368" />

## Introduction

This room will introduce you to 3 elements of the OWASP Top 10 list (2025). In this room, you will learn about the elements relating to application behaviour and user input. We will cover these vulnerabilities briefly, how to prevent them, and finally, you will practice exploiting these vulnerabilities:
- A04: Cryptographic Failures
- A05: Injection
- A08: Software or Data Integrity Failures

---

### Deploy Practical

Start the Lab Machine and I am using my Kali Linux Machine as an Attack Box, so I will connect my machine to the TryHackMe Server by OpenVPN.

You can check how to connect your machine by OpenVPN through this room: [OpenVPN](https://tryhackme.com/room/openvpn)

Connecting by command: `sudo openvpn <filename>`

## A04: Cryptographic Failures

**What are Cryptographic Failures?**

Cryptographic failures happen when sensitive data isn't adequately protected due to lack of encryption, faulty implementation, or insufficient security measures. This includes storing passwords without hashing, using outdated or weak algorithms (such as MD5, SHA1, or DES), exposing encryption keys, or failing to secure data during transmission.

A good example is when a company creates its own encryption method instead of using trusted and well-tested encryption algorithms. Their custom encryption is often less secure and can contain weaknesses that attackers can exploit.

**How to Prevent Cryptographic Failures**

Preventing cryptographic failures starts with choosing strong, modern algorithms and implementing them properly. Sensitive information such as passwords should be hashed using robust, slow hashing functions like bcrypt, scrypt, or Argon2. When encrypting data, avoid creating your own algorithms; instead, rely on trusted, industry-standard libraries.

Never embed access credentials (i.e., to a third-party service) in source code, configuration files, or repositories. Instead, use secure key management systems or environments specifically designed for storing secrets.

---

### Practical

The practical for this task is located at `http://MACHINE_IP:8001`. This web app demonstrates a "note sharing" service that uses a weak, shared derivative key to protect the notes.

Follow the steps on the web application to unlock all notes and retrieve a flag.

---

### Recommended TryHackMe Content

If you'd like to explore this type of attack in much further depth, we highly recommend the following TryHackMe content: [Cryptographic Failures Module](https://tryhackme.com/module/cryptofailures)

---

### Answer the questions below

Decrypt the encrypted notes. One of them will contain a flag value. What is it?

Navigating to the page gives us hint that it uses Weak XOR Cipher where the first three characters of the ket is `KEY`, we just need to guess the 4th character of the key.

I created a small python script `decode.py` which bruteforces letters and numbers and we get readable english in `KEY1`:

<img width="362" height="335" alt="image" src="https://github.com/user-attachments/assets/e288fbeb-d60a-482b-91e0-3ffff61587fc" />

<img width="808" height="625" alt="image" src="https://github.com/user-attachments/assets/2f4590fc-b3b8-4971-9b7c-31a294c9295d" />



