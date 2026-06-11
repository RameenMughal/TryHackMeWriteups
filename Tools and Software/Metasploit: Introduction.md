# Metasploit: Introduction

Room: [Metasploit: Introduction](https://tryhackme.com/room/metasploitintro)

<img width="1873" height="386" alt="image" src="https://github.com/user-attachments/assets/2144cff7-b2a2-4c31-8e45-4d19d71a88d2" />

## Introduction to Metasploit

Metasploit is the most widely used exploitation framework. Metasploit is a powerful tool that can support all phases of a penetration testing engagement, from information gathering to post-exploitation.

Metasploit has two main versions:
- **Metasploit Pro**: The commercial version that facilitates the automation and management of tasks. This version has a graphical user interface (GUI).
- **Metasploit Framework**: The open-source version that works from the command line. It is most commonly used penetration testing Linux distributions.

The Metasploit Framework is a set of tools that allow information gathering, scanning, exploitation, exploit development, post-exploitation, and more. 

While the primary usage of the Metasploit Framework focuses on the penetration testing domain, it is also useful for vulnerability research and exploit development.

The main components of the Metasploit Framework can be summarized as follows;
- **msfconsole**: The main command-line interface.
- **Modules**: supporting modules such as exploits, scanners, payloads, etc.
- **Tools**: Stand-alone tools that will help vulnerability research, vulnerability assessment, or penetration testing. Some of these tools are `msfvenom`, `pattern_create` and `pattern_offset`.

We will cover `msfvenom` within this module, but `pattern_create` and `pattern_offset` are tools useful in exploit development which is beyond the scope of this module.

## Main Components of Metasploit

While using the Metasploit Framework, you will primarily interact with the Metasploit console. You can launch it from the AttackBox terminal or your Machine using the `msfconsole` command. The console will be your main interface to interact with the different modules of the Metasploit Framework. 

<img width="367" height="349" alt="image" src="https://github.com/user-attachments/assets/aea2b88c-1e51-4bc9-a34e-0047b6c0165a" />

Modules are small components within the Metasploit framework that are built to perform a specific task, such as exploiting a vulnerability, scanning a target, or performing a brute-force attack.

Before diving into modules, it would be helpful to clarify a few recurring concepts: vulnerability, exploit, and payload.
- **Exploit**: A piece of code that uses a vulnerability present on the target system.
- **Vulnerability**: A design, coding, or logic flaw affecting the target system. The exploitation of a vulnerability can result in disclosing confidential information or allowing the attacker to execute code on the target system.
- **Payload**: An exploit will take advantage of a vulnerability. However, if we want the exploit to have the result we want (gaining access to the target system, read confidential information, etc.), we need to use a payload. Payloads are the code that will run on the target system.

Think of it this way:
- Exploit = The way to break in
- Payload = What you do after breaking in

**Simple Formula**: Exploit + Payload = Access

Modules and categories under each one are listed below. These are given for reference purposes, but you will interact with them through the Metasploit console (`msfconsole`).

---

### Auxiliary

Any supporting module, such as scanners, crawlers and fuzzers, can be found here.

Crawlers work like automated web spiders. Their purpose is to enumerate and map web applications by systematically visiting pages, following links, and collecting information about the structure and content of the target site.

Fuzzers are auxiliary modules designed to automatically send lots of varied, often malformed or unexpected input to a target application, service, or protocol in order to:
- Discover crashes (which may reveal vulnerabilities).
- Test robustness of an application (how well it handles unexpected input).
- Find buffer overflows, format string bugs, or injection points.

Checking the options for Auxiliary module: `tree -L 1 /usr/share/metasploit-framework/modules/auxiliary`

<img width="328" height="256" alt="image" src="https://github.com/user-attachments/assets/d8aeb099-431f-4ebf-a073-f325009c2e0f" />

---

### Encoders

Encoders will allow you to encode the exploit and payload in the hope that a signature-based antivirus solution may miss them.

Signature-based antivirus and security solutions have a database of known threats. They detect threats by comparing suspicious files to this database and raise an alert if there is a match. Thus encoders can have a limited success rate as antivirus solutions can perform additional checks.

Checking the options for Encoders module: `tree -L 1 /usr/share/metasploit-framework/modules/encoders`

<img width="328" height="147" alt="image" src="https://github.com/user-attachments/assets/ff5abb6b-2d82-44b2-a8c7-10a12870ea81" />

---

### Evasion

While encoders will encode the payload, they should not be considered a direct attempt to evade antivirus software. On the other hand, “evasion” modules will try that, with more or less success.

An Evasion Module in Metasploit is used to help a payload avoid detection by antivirus (AV), endpoint protection, or security software.

Checking the options for Evasion module: `tree -L 2 /usr/share/metasploit-framework/modules/evasion`

<img width="320" height="148" alt="image" src="https://github.com/user-attachments/assets/e0861a64-f09f-4814-b770-023f5a9fbb9a" />

---

### Exploits

Exploits, neatly organized by target system.

Checking the options for Exploits module: `tree -L 1 /usr/share/metasploit-framework/modules/exploits`

<img width="329" height="290" alt="image" src="https://github.com/user-attachments/assets/fde39eb2-73f8-42bc-87e4-c06e39e30c44" />

---

### NOPs

NOPs (No OPeration) do nothing, literally. They are represented in the Intel x86 CPU family with 0x90, following which the CPU will do nothing for one cycle. They are often used as a buffer to achieve consistent payload sizes.

Checking the options for NOPs module: `tree -L 1 /usr/share/metasploit-framework/modules/nops`

<img width="305" height="169" alt="image" src="https://github.com/user-attachments/assets/c4cf8ecc-b5f5-41ef-81dd-3922e73b158c" />

---

### Payloads

Payloads are codes that will run on the target system.

Exploits will leverage a vulnerability on the target system, but to achieve the desired result, we will need a payload. 

Examples could be; getting a shell, loading a malware or backdoor to the target system, running a command, or launching calc.exe as a proof of concept to add to the penetration test report. 

Running command on the target system is already an important step but having an interactive connection that allows you to type commands that will be executed on the target system is better. Such an interactive command line is called a "shell". Metasploit offers the ability to send different payloads that can open shells on the target system.

Checking the options for Payloads module: `tree -L 1 /usr/share/metasploit-framework/modules/payloads`

<img width="329" height="85" alt="image" src="https://github.com/user-attachments/assets/f66f2ee8-fc59-4a86-bbfa-4cae0ff5a349" />

- **Adapters**: Change a payload into another form, such as a PowerShell command.
- **Singles**: A complete payload that works by itself and doesn't need anything else.
- **Stagers**: A small payload that connects to the attacker and downloads the real payload.
- **Stages**: The main payload that gets downloaded by the stager.

Metasploit has a subtle way to help you identify single (also called “inline”) payloads and staged payloads.

- **Single Payload (`_`)**: Contains everything needed and runs immediately. Example: `shell_reverse_tcp`
- **Staged Payload (`/`)**: Sent in two parts—a small stager first, then the main payload. Example: `shell/reverse_tcp`

---

### Post

Post modules will be useful on the final stage of the penetration testing process listed above, post-exploitation.

Checking the options for Post module: `tree -L 1 /usr/share/metasploit-framework/modules/post`

<img width="298" height="167" alt="image" src="https://github.com/user-attachments/assets/8df6c953-7453-47c7-a568-6d71015c064b" />












