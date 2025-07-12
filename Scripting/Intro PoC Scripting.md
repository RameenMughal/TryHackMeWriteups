# Intro PoC Scripting

## Introduction – What are PoC Scripts?

This room is an introduction to a fundamental skill of most cybersecurity domains; exploit development by crafting exploit scripts from proof of concept code.

**proof of concept (PoC)**: evidence, typically derived from an experiment or pilot project, which demonstrates that a design concept, business proposal, etc., is feasible.

A Proof of Concept (PoC) is a small test or trial that shows your idea can actually work in real life.

Not every vulnerability that exists will have a pre-made exploit script to use but, if you learn and practice how to make them yourself, you'll acquire a deeper understanding of cybersecurity topics and accumulate more technical skills.

### Methodologies

A handful of common methodologies I've found thus far include:
- Optimize the script and condense unnecessary code: keep it simple stupid
- Read and reread PoC code before researching: assists in identifying errors in scripts and how to fix them, sometimes before they occur
- Research as detailed as possible: not all essential information is found on documentation and stackoverflow
- Prepare to adapt and customize: PoC code sometimes uses pre-made libraries with specific functions you'll need to personally craft
- Test segments of code along the way: this makes it easier to pinpoint potential issues

## Example – The Starting Point

In terms of CTFs, vulnerability scanning, penetration testing, and across an extensive array of security fields, writing PoC scripts can be used to assist or completely accomplish one's task a majority of the time.

Credentials 

username: user1

password: 1user

We can use a native Kali tool `searchsploit` to inspect the platform and version number, it parses the exploit-db website for known exploits.

`searchsploit webmin 1.580`

The module exploits an arbitrary command execution vulnerability in Webmin 1.580, CVE-2012-2982. The vulnerability exists in the `/file/show.cgi` component and allows an authenticated user, with access to the File Manager Module, to execute arbitrary commands with root privileges.

On the surface level, we know that we can execute any program we want on this Ubuntu server. In most scenarios it makes sense to execute the system shell, especially when we have root or administrator privileges. It enables us to have complete control over the target system and manipulate it to our needs.

This means that an input invalidation flaw within the binary file of `show.cgi`, exploited using a | (pipe) character, allows for remote authenticated attackers to execute any command as a privileged user. Meaning all we need to do is input invalid characters and pipe those to a system command (system shell). We can execute the payload, open a socket connection and send it back to the attacker listening with `netcat`

### Answer the questions below

1. What is the target's platform and version number?

Webmin 1.580

3. What is the associated CVE for this platform?

CVE-2012-2982

5. Which file does the vulnerability exist in?

`file/show.cgi`

7. What program/command would be the most effective to use in this exploit?

System shell
