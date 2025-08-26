# Metasploit: Introduction

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

While using the Metasploit Framework, you will primarily interact with the Metasploit console. You can launch it from the AttackBox terminal using the `msfconsole` command. The console will be your main interface to interact with the different modules of the Metasploit Framework. 

Modules are small components within the Metasploit framework that are built to perform a specific task, such as exploiting a vulnerability, scanning a target, or performing a brute-force attack.

Before diving into modules, it would be helpful to clarify a few recurring concepts: vulnerability, exploit, and payload.
- **Exploit**: A piece of code that uses a vulnerability present on the target system.
- **Vulnerability**: A design, coding, or logic flaw affecting the target system. The exploitation of a vulnerability can result in disclosing confidential information or allowing the attacker to execute code on the target system.
- **Payload**: An exploit will take advantage of a vulnerability. However, if we want the exploit to have the result we want (gaining access to the target system, read confidential information, etc.), we need to use a payload. Payloads are the code that will run on the target system.

Modules and categories under each one are listed below. These are given for reference purposes, but you will interact with them through the Metasploit console (`msfconsole`).

### Auxiliary

Any supporting module, such as scanners, crawlers and fuzzers, can be found here.

Crawlers work like automated web spiders. Their purpose is to enumerate and map web applications by systematically visiting pages, following links, and collecting information about the structure and content of the target site.

Fuzzers are auxiliary modules designed to automatically send lots of varied, often malformed or unexpected input to a target application, service, or protocol in order to:
- Discover crashes (which may reveal vulnerabilities).
- Test robustness of an application (how well it handles unexpected input).
- Find buffer overflows, format string bugs, or injection points.

Checking the options for Auxiliary module `ls -d /usr/share/metasploit-framework/modules/auxiliary/*/`

<img width="836" height="85" alt="image" src="https://github.com/user-attachments/assets/37176884-6e4a-451c-97be-b4122994b1a4" />

