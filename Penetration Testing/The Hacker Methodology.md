# The Hacker Methodology

## Methodology Outline

Professional hackers/penetration tester generally follow an established process to understand and exploit their targets. 

The process that pentesters follow is summarized in the following steps:

1. Reconnaissance  
2. Enumeration/Scanning  
3. Gaining Access  
4. Privilege Escalation  
5. Covering Tracks  
6. Reporting

### Answer the questions below

What is the first phase of the Hacker Methodology? 

Reconnaissance

## Reconnaissance

The first phase of the Ethical Hacker Methodology is the Reconnaissance.

Reconnaissance is all about collecting information about your target.

Reconnaissance usually involves no interaction with the target(s) or system(s). 

Following tools are frequently used for this phase

- Google (specifically Google Dorking)
- Wikipedia
- PeopleFinder.com
- who.is
- sublist3r
- hunter.io
- builtwith.com
- wappalyzer

### Answer the questions below

1. Who is the CEO of SpaceX?

Elon Musk

2. Do some research into the tool: sublist3r, what does it list?

subdomains

3. What is it called when you use Google to look for specific vulnerabilities or to research a specific topic of interest?

Google Dorking

## Enumeration and Scanning Overview

The second phase of the Hacker Methodology is Scanning and Enumeration.

This is where a hacker will start interacting with (scanning and enumerating) the target to attempt to find vulnerabilities related to the target.

Tools like nmap, dirb, metasploit, exploit-db, Burp Suite and others are very useful to help us try to find vulnerabilities in a target. 

In the scanning and enumeration phase, the attacker is interacting with the target to determine its overall attack surface.

The attack surface determines what the target might be vulnerable to in the Exploitation phase.

For example, one important tool in our arsenal is a tool called Nmap

Nmap is a tool which can scan a target and tell us a wide variety of things:
- What ports are open
- The operating system of the target (Windows, Linux, MacOS, etc.)
- What services are running and what version of the service

Here is a quick sampling of other tools that you can learn:
- dirb (used to find commonly-named directories on a website - like how under https://www.tesla.com there is)
- dirbuster (similar to dirb but with a cooler name, and with a user interface)
- enum4linux (tool used specifically for Linux to find vulnerabilities)
- metasploit (this tool is mostly used for exploitation, but it also has some built-in enumeration tools)
- Burp Suite (this tool can be used to scan a website for subdirectories and to intercept network traffic)

### Answer the questions below

1. What does enumeration help to determine about the target?

Attack Surface

2. Do some reconnaissance about the tool: Metasploit, what company developed it? 

Rapid7

3. What company developed the technology behind the tool Burp Suite?

PortSwigger

## Exploitation

One common tool used for exploitation is called Metasploit which has many built-in scripts to try to keep life simple.

You can also used tools like Burp Suite and SQLMap to exploit web applications. There are tools such as msfvenom (for building custom payloads), BeEF (browser-based exploitation), and many many others.

### Answer the questions below

What is one of the primary exploitation tools that pentester(s) use? 

Metasploit

## Privilege Escalation

After we have gained access to a victim machine via the exploitation phase, the next step is to escalate privileges to a higher user account. The following accounts are what we try to reach as a pentester:
- In the Windows world, the target account is usually: Administrator or System.
- In the Linux world, the target account is usually: root

Privilege escalation can take many, many forms, some examples are:
- Cracking password hashes found on the target
- Finding a vulnerable service or version of a service which will allow you to escalate privilege THROUGH the service
- Password spraying of previously discovered credentials (password re-use)
- Using default credentials
- Finding secret keys or SSH keys stored on a device which will allow pivoting to another machine
- Running scripts or commands to enumerate system settings like `ifconfig` to find network settings, or the command `find / -perm
-4000 -type f 2>/dev/null` to see if the user has access to any commands they can run as root

### Answer the questions below

1. In Windows what is usually the other target account besides Administrator?

System

2. What thing related to SSH could allow you to login to another machine (even without knowing the username or password)?

Keys

## Covering Tracks

You should always have explicit permission from the system owner regarding when the test is happening, how its occurring, and the scope of targets in any penetration test.

Since the rules of engagement for a penetration test should be agreed to before the test occurs, the penetration tester should stop IMMEDIATELY when they have achieved privilege escalation and report the finding to the client. 

While ethical hackers rarely have a need to cover their tracks, you still must carefully track and notate all of the tasks that you performed as part of the penetration test to assist in fixing the vulnerabilities and recommending changes to the system owner.

## Reporting

The final phase of the pentest methodology is the reporting phase.

This is one of the most important phases where you will outline everything that you found. The reporting phase often includes the following things:
- The Finding(s) or Vulnerabilities
- The CRITICALITY of the Finding
- A description or brief overview of how the finding was discovered
- Remediation recommendations to resolve the finding

The amount of reporting documentation varies widely by the type of engagement that the pentester is involved in. A findings report generally goes in three formats:
- Vulnerability scan results (a simple listing of vulnerabilities)
- Findings summary (list of the findings as outlined above)
- Full formal report.

### Answer the questions below

1. What would be the type of reporting that involves a full documentation of all findings within a formal document?

Full Formal Report

2. What is the other thing that a pentester should provide in a report beyond: the finding name, the finding description, the finding criticality.

Remediation Recommendation
