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

---

### Answer the questions below

1. What is the name of the code taking advantage of a flaw on the target system?

Exploit

2. What is the name of the code that runs on the target system to achieve the attacker's goal?

Payload

3. What are self-contained payloads called?

Singles

4. Is "windows/x64/pingback_reverse_tcp" among singles or staged payload?

Singles

## Msfconsole

The console will be your main interface to the Metasploit Framework. You can launch it using the `msfconsole` command on your AttackBox terminal or any system the Metasploit Framework is installed on.

<img width="367" height="349" alt="image" src="https://github.com/user-attachments/assets/aea2b88c-1e51-4bc9-a34e-0047b6c0165a" />

It will support most Linux commands, including `clear` (to clear the terminal screen), but will not allow you to use some features of a regular command line (e.g. does not support output redirection).

The `help` command can be used on its own or for a specific command.

You can use the `history` command to see commands you have typed earlier.

Msfconsole is managed by context; this means that unless set as a global variable, all parameter settings will be lost if you change the module you have decided to use. 

In the example below, we have used the `ms17_010_eternalblue` exploit, and we have set parameters such as `RHOSTS`. If we were to switch to another module (e.g. a port scanner), we would need to set the `RHOSTS` value again as all changes we have made remained in the context of the `ms17_010_eternalblue` exploit. 

Let us look at the example below to have a better understanding of this feature. We will use the MS17-010 “Eternalblue” exploit for illustration purposes.

Once you type the `use exploit/windows/smb/ms17_010_eternalblue` command, you will see the command line prompt change from msf6 to `msf6 exploit(windows/smb/ms17_010_eternalblue)`. 

The "EternalBlue" is an exploit allegedly developed by the U.S. National Security Agency (N.S.A.) for a vulnerability affecting the SMBv1 server on numerous Windows systems. The SMB (Server Message Block) is widely used in Windows networks for file sharing and even for sending files to printers. EternalBlue was leaked by the cybercriminal group "Shadow Brokers" in April 2017. In May 2017, this vulnerability was exploited worldwide in the WannaCry ransomware attack.

<img width="396" height="41" alt="image" src="https://github.com/user-attachments/assets/d674aa41-610c-4189-b019-f20d90170e85" />

The module to be used can also be selected with the `use` command followed by the number at the beginning of the search result line.

<img width="851" height="254" alt="image" src="https://github.com/user-attachments/assets/eb7923a1-2b2e-4e93-b5a1-27c56ebbcab6" />

<img width="593" height="74" alt="image" src="https://github.com/user-attachments/assets/dea01330-a781-41bc-b31f-6bcbeedc0281" />

While the prompt has changed, you will notice we can still run the commands previously mentioned. This means we did not "enter" a folder as you would typically expect in an operating system command line.

The prompt tells us we now have a context set in which we will work. You can see this by typing the show options command.

```
msf exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded
                                             Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Stan
                                             dard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 tar
                                             get machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     192.168.50.128   yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf exploit(windows/smb/ms17_010_eternalblue) > 
```

This will print options related to the exploit we have chosen earlier. The show options command will have different outputs depending on the context it is used in. The example above shows that this exploit will require we set variables like RHOSTS and RPORT. 

On the other hand, a post-exploitation module may only need us to set a SESSION ID. A session is an existing connection to the target system that the post-exploitation module will use.

The `show` command can be used in any context followed by a module type (auxiliary, payload, exploit, etc.) to list available modules. The example below lists payloads that can be used with the ms17-010 Eternalblue exploit.

<img width="845" height="305" alt="image" src="https://github.com/user-attachments/assets/e0ded24b-6a84-4147-ab09-5a4aeea53fb4" />

You can leave the context using the `back` command.

<img width="281" height="38" alt="image" src="https://github.com/user-attachments/assets/f4dc093c-4951-4ad3-93bc-576d1bbc3a26" />

Further information on any module can be obtained by typing the `info` command within its context.

```
msf exploit(windows/smb/ms17_010_eternalblue) > info

       Name: MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
     Module: exploit/windows/smb/ms17_010_eternalblue
   Platform: Windows
       Arch: x64
 Privileged: Yes
    License: Metasploit Framework License (BSD)
       Rank: Average
  Disclosed: 2017-03-14

Provided by:
  Equation Group
  Shadow Brokers
  sleepya
  Sean Dillon <sean.dillon@risksense.com>
  Dylan Davis <dylan.davis@risksense.com>
  thelightcosine
  wvu <wvu@metasploit.com>
  agalway-r7
  cdelafuente-r7
  cdelafuente-r7
  agalway-r7

Module side effects:
 unknown-side-effects

Module stability:
 unknown-stability

Module reliability:
 unknown-reliability

Available targets:
      Id  Name
      --  ----
  =>  0   Automatic Target
      1   Windows 7
      2   Windows Embedded Standard 7
      3   Windows Server 2008 R2
      4   Windows 8
      5   Windows 8.1
      6   Windows Server 2012
      7   Windows 10 Pro
      8   Windows 10 Enterprise Evaluation

Check supported:
  Yes

Basic options:
  Name           Current Setting  Required  Description
  ----           ---------------  --------  -----------
  RHOSTS                          yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
  RPORT          445              yes       The target port (TCP)
  SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded S
                                            tandard 7 target machines.
  SMBPass                         no        (Optional) The password for the specified username
  SMBUser                         no        (Optional) The username to authenticate as
  VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Stand
                                            ard 7 target machines.
  VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 targ
                                            et machines.

Payload information:
  Space: 2000

Description:
  This module is a port of the Equation Group ETERNALBLUE exploit, part of
  the FuzzBunch toolkit released by Shadow Brokers.

  There is a buffer overflow memmove operation in Srv!SrvOs2FeaToNt. The size
  is calculated in Srv!SrvOs2FeaListSizeToNt, with mathematical error where a
  DWORD is subtracted into a WORD. The kernel pool is groomed so that overflow
  is well laid-out to overwrite an SMBv1 buffer. Actual RIP hijack is later
  completed in srvnet!SrvNetWskReceiveComplete.

  This exploit, like the original may not trigger 100% of the time, and should be
  run continuously until triggered. It seems like the pool will get hot streaks
  and need a cool down period before the shells rain in again.

  The module will attempt to use Anonymous login, by default, to authenticate to perform the
  exploit. If the user supplies credentials in the SMBUser, SMBPass, and SMBDomain options it will use
  those instead.

  On some systems, this module may cause system instability and crashes, such as a BSOD or
  a reboot. This may be more likely with some payloads.

References:
  https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2017/MS17-010
  https://nvd.nist.gov/vuln/detail/CVE-2017-0143
  https://nvd.nist.gov/vuln/detail/CVE-2017-0144
  https://nvd.nist.gov/vuln/detail/CVE-2017-0145
  https://nvd.nist.gov/vuln/detail/CVE-2017-0146
  https://nvd.nist.gov/vuln/detail/CVE-2017-0147
  https://nvd.nist.gov/vuln/detail/CVE-2017-0148
  https://github.com/RiskSense-Ops/MS17-010
  https://risksense.com/wp-content/uploads/2018/05/White-Paper_Eternal-Blue.pdf
  https://www.exploit-db.com/exploits/42030
  https://attack.mitre.org/techniques/T1059/
  https://attack.mitre.org/techniques/T1068/
  https://attack.mitre.org/techniques/T1210/

Also known as:
  ETERNALBLUE


View the full module info with the info -d command.

msf exploit(windows/smb/ms17_010_eternalblue) > 
```

Alternatively, you can use the info command followed by the module’s path from the msfconsole prompt (e.g. `info exploit/windows/smb/ms17_010_eternalblue`). 

Info is not a help menu; it will display detailed information on the module such as its author, relevant sources, etc.

---

### Search

One of the most useful commands in msfconsole is `search`. This command will search the Metasploit Framework database for modules relevant to the given search parameter. You can conduct searches using CVE numbers, exploit names (eternalblue, heartbleed, etc.), or target system.

<img width="854" height="309" alt="image" src="https://github.com/user-attachments/assets/fdddf842-ab37-4b95-ae4b-630d91b811cd" />

The output of the `search` command provides an overview of each returned module. You may notice the “name” column already gives more information than just the module name. You can see the type of module (auxiliary, exploit, etc.) and the category of the module (scanner, admin, windows, Unix, etc.). 

You can use any module returned in a search result with the command use followed by the number at the beginning of the result line. (e.g. `use 0` instead of `use auxiliary/admin/smb/ms17_010_command`)

Another essential piece of information returned is in the “rank” column. Exploits are rated based on their reliability. The table below provides their respective descriptions.

| Ranking | Easy Meaning |
|----------|-------------|
| **Excellent** | Very reliable. Almost never crashes the target and works consistently. |
| **Great** | Very reliable and usually detects the correct target/version automatically. |
| **Good** | Reliable for common versions of the software. |
| **Normal** | Works, but you must know the exact version/configuration of the target. |
| **Average** | Unreliable; may fail often or be difficult to use. |
| **Low** | Rarely works (less than 50% success rate). |
| **Manual** | Requires manual setup and may be unstable. |

**Easy order to remember:** `Excellent > Great > Good > Normal > Average > Low > Manual`

You can direct the search function using keywords such as `type` and `platform`.

For example, if we wanted our search results to only include auxiliary modules, we could set the `type` to auxiliary. The screenshot below shows the output of the `search type:auxiliary telnet` command.

<img width="857" height="307" alt="image" src="https://github.com/user-attachments/assets/9ffe46c0-3336-4aa3-b8c5-6f52bfed1c31" />

Please remember that exploits take advantage of a vulnerability on the target system and may always show unexpected behavior. A low-ranking exploit may work perfectly, and an excellent ranked exploit may not, or worse, crash the target system.

---

### Answer the questions below

1. How would you search for a module related to Apache?

`search apache`

<img width="851" height="283" alt="image" src="https://github.com/user-attachments/assets/b622c722-b19c-4bec-aa8a-7b5dcb13c784" />

2. Who provided the auxiliary/scanner/ssh/ssh_login module?

todb

Write `info auxiliary/scanner/ssh/ssh_login` to get information about this

<img width="259" height="134" alt="image" src="https://github.com/user-attachments/assets/50f65a17-ca15-437a-bc02-754a863a887c" />


























