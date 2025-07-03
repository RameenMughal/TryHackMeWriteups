# Linux Strength Training

## Finding your way around Linux – Overview

As a security researcher you will often be required to find specific files/folders on a system based on various conditions ranging from, but not limited to the following:
- filename
- size
- user/group
- date modified
- date accessed
- Its keyword contents

We can do this using the following syntax:

| Description                            | Syntax                                                       | Example                                                                                                                                                   |
|----------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Find files by filename                 | `find [directory path] -type f -name [filename]`             | `find /home/Andy -type f -name sales.txt`                                                                                                                 |
| Find directories by name               | `find [directory path] -type d -name [filename]`             | `find /home/Andy -type d -name pictures`                                                                                                                  |
| Find files by size                     | `find [directory path] -type f -size [size]`                 | `find /home/Andy -type f -size 10c`                                                                                                                       |
|                                        |                                                              | *(c=bytes, k=KB, M=MB, G=GB)*                                                                                                                             |
| Find files by username                 | `find [directory path] -type f -user [username]`             | `find /etc/server -type f -user john`                                                                                                                     |
| Find files by group name               | `find [directory path] -type f -group [group]`               | `find /etc/server -type f -group teamstar`                                                                                                                |
| Find files modified after a date       | `find [directory path] -type f -newermt '[date and time]'`   | `find / -type f -newermt '6/30/2020 0:00:00'`                                                                                                             |
|                                        |                                                              | All dates/times after 6/30/2020 0:00:00 will be considered a condition to look for                                                                        |
| Find files modified within date range  | `find [dir] -type f -newermt [start] ! -newermt [end]`       | `find / -type f -newermt 2013-09-12 ! -newermt 2013-09-14`                                                                                                |
|                                        |                                                              | All dates before 2013-09-12 will be excluded; all dates after 2013-09-14 will be excluded, therefore this only leaves 2013-09-13 as the date to look for. |
| Find files accessed within date range  | `find [dir] -type f -newerat [start] ! -newerat [end]`       | `find / -type f -newerat 2017-09-12 ! -newerat 2017-09-14`                                                                                                |
|                                        |                                                              | All dates before 2017-09-12 will be excluded; all dates after 2017-09-14 will be excluded, therefore this only leaves 2017-09-13 as the date to look for. |
| Find files with specific keyword       | `grep -iRl [directory path/keyword]`                         | `grep -iRl '/folderA/flag'`                                                                                                                               |

**Notes**: Typing CTRL+L allows you to clear the screen quicker rather than typing 'clear' all the time.

Placing: `2>/dev/null` at the end of your find command can help filter your results to exclude files/directories that you do not have permission to.

### Answer the questions below

1. What is the correct option for finding files based on group.

`-group`

2. What is format for finding a file with the user named Francis and with a size of 52 kilobytes in the directory /home/francis/

`find /home/francis -type f -user Francis -size 52k`

3. . SSH as topson using his password topson. Go to the /home/topson/chatlogs directory and type the following: `grep -iRl 'keyword'`. What is the name of the file that you found using this command?

`ssh topson@10.10.187.108` (Your target machine IP address)

Moving to the chatlogs directory

`grep -iRl 'keyword'`

![image](https://github.com/user-attachments/assets/ae783e0c-8eb9-418d-82bf-d74e72a8dbb2)

**Answer**: 2019-10-11

4. Type: `less [filename]` to open the file. Then, before anything, type / before typing: keyword followed by [ENTER]. Notice how that allowed us to search for the first instance of that word in the entire document. For much larger documents this can be useful and if there are many more instances of that word in the document, we would be able to hit enter again to find the next instance in the document.

`less 2019-10-11`

`/keyword` then Enter

5. What are the characters subsequent to the word you found?

ttitor

6. Read the file named 'ReadMeIfStuck.txt'. What is the Flag?

Checking where the ReadMeIfStuck.txt is 

![image](https://github.com/user-attachments/assets/1faee3e3-f512-4545-bbd1-fedcb9179e63)

Finding the additionalHINT file `find / -type f -name additionalHINT 2>/dev/null`

![image](https://github.com/user-attachments/assets/7347715e-54a1-4f66-820a-fb186cf80daa)

Going to the channels directory and checking the content of additionalHINT

![image](https://github.com/user-attachments/assets/f8d744df-6e4b-4b4f-8b85-718a3c6fefc8)

Finding the telephone numbers directory

![image](https://github.com/user-attachments/assets/8e6af2a0-c601-49a9-8679-c270091edf37)

Going to the telephone numbers directory and checking the content of file

![image](https://github.com/user-attachments/assets/1cfc395a-9644-4462-bb0d-ec2f44debd59)

Finding the file in workflow directory of modified date, first finding the workflow directory

`find / -type d -name workflows 2>>/dev/null`

![image](https://github.com/user-attachments/assets/a6acb1d9-1765-4800-9e79-f3fa5cc9bc85)

Now finding the file modified `find / -type f -newermt 2016-09-11 ! -newermt 2016-09-13 2>/dev/null`

![image](https://github.com/user-attachments/assets/dd4ff8fe-f181-4b7b-afb0-0e001bf53616)

The first file is the one, going to the xft directory and get the content with the less command `less eBQRhHvx`

Search `/Flag`, scroll down and you get the flag 

![image](https://github.com/user-attachments/assets/c9faaaef-989a-41b1-94ef-6525192025f0)

## Working with files

For a quick recap to train your mental memory on the commands please refer to the below information:

| Description                                 |   Syntax                                                                     |   Example                                                         |
|---------------------------------------------|-------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Copy file/folder                             | `cp [filename/folder] [directory]`                                           | `cp ssh.conf /home/newfolder`                                     |
| (With spaces in filename)                    | `cp "[filename with spaces]" [directory]`                                    | `cp "ssh config.conf" /home/newfolder`                            |
| Move file/folder                             | `mv [filename] [directory]`                                                  | `mv ssh.conf /home/newfolder`                                     |
| Move multiple files/folders simultaneously   | `mv [file1] [file2] [file3] -t [directory]`                                   | `mv logs.txt keys.conf script.py -t /home/savedWork`              |
| Move all files from current directory        | `mv * [directory]`                                                           | `mv * /home/scripts`                                              |
| Rename file/folder                           | `mv [current filename] [new filename]`                                       | `mv ssh.conf NewSSH.conf`                                         |
| Create a file                                | `touch [filename]`                                                           | `touch newFile.txt`                                               |
| Create a folder                              | `mkdir [foldername]`                                                         | `mkdir newFolder`                                                 |
| Open file for editing                        | `nano [filename]`                                                            | `nano keys.conf`                                                  |
| Output contents of file                      | `cat [filename]`                                                             | `cat keys.conf`                                                   |
| Upload file to remote machine (via SCP)      | `scp [file] [user]@[IP]:/[target directory]`                                 | `scp example.txt john@192.168.100.123:/home/john/`                |
| Run a Bash script                            | `./[script name]`                                                            | `./timer`                                                         |

A few additional things to remember is that occasionally you may encounter files/folders with special characters such as - (dash). Just remember that if you try to copy or move these files you will encounter errors because Linux interprets the - as a type of argument, therefore you will have to place `--` just before the filename.

### Answer the questions below

1. Hypothetically, you find yourself in a directory with many files and want to move all these files to the directory of /home/francis/logs. What is the correct command to do this?

`mv * /home/francis/logs`

2. Hypothetically, you want to transfer a file from your /home/james/Desktop/ with the name script.py to the remote machine (192.168.10.5) directory of /home/john/scripts using the username of john. What would be the full command to do this?

`scp /home/james/Desktop/ script.py john@192.168.10.5:/home/john/scripts`

3. How would you rename a folder named -logs to -newlogs

`mv -- -logs -newlogs`

4. How would you copy the file named encryption keys to the directory of /home/john/logs

`cp “encryption keys” /home/john/logs`

5. Find a file named readME_hint.txt inside topson's directory and read it. Using the instructions it gives you, get the second flag.

Finding the readME_hint.txt `find / -type f -name readME_hint.txt 2>/dev/null`

![image](https://github.com/user-attachments/assets/ec5eee79-74aa-417a-98aa-930ddff14cab)

Moving -MoveMe.txt to the -march folder directory `mv -- -MoveMe.txt '-march folder'`

Checking the -march folder directory and running the sh program

![image](https://github.com/user-attachments/assets/da6bfa0f-0e62-4db6-a790-f5c58225a50e)

![image](https://github.com/user-attachments/assets/916a4866-16f0-4e6a-a974-1396d63622f5)

## Hashing – Introduction

Hashing refers to taking any data input, such as a password and calculating its hash equivalent. 

The hash equivalent is a long string which cannot be reversed since the act of hashing is known as a one-way function.

One of hashing algorithm is MD5.

Message Digest 5 (MD5) is a cryptographic hash function that takes any input and produces a 128-bit hexadecimal number. The output of an MD5 hash function is called a digest. 

However, MD5 is no longer considered secure and should not be used for sensitive applications.

**Note**: MD5 and SHA1 are both examples of weak hash algorithms which have been proven to be vulnerable to something known as hash collision attacks.

Hashes can be cracked through the method of brute-forcing. 

This essentially means using a wordlist and inputting each potential password from the wordlist into the hash function to see if we get a hash equivalent output that is equal to any of the hashes stored in the database.

John the Ripper is a free and open-source password-cracking tool. It can crack passwords stored in various formats, including hashes, passwords, and encrypted private keys. It can be used to test passwords' security and recover lost passwords.

If you ever encounter a hash that you do not know the type of you can use a tool called hash-identifier.

However, with less widely used hashes the tool will not be accurate and therefore will still rely on you to develop the skill of manually identifying what type of hash it is.

Syntax: `hash-identifier [hash]`

You could pipe the output of the file storing the hash to hash-identifier.

`cat hash.txt | hash-identifier`

### Answer the questions below

1. Download the hash file attached to this task and attempt to crack the MD5 hash. What is the password?

Checking through Crackstation website, secret123

2. SSH as sarah using: sarah@[MACHINE_IP] and use the password: rainbowtree1230x. What is the hash type stored in the file hashA.txt

Finding the hashA.txt `find / -type f -name hashA.txt 2>/dev/null`

![image](https://github.com/user-attachments/assets/e7711e4e-518b-48e3-bbe7-46f0c0aefdaa)

Going to the server settings directory and checking the content of hashA.txt which is `f9d4049dd6a4dc35d40e5265954b2a46`

Checking which hash it is by hash-identifier `hash-identifier f9d4049dd6a4dc35d40e5265954b2a46`

![image](https://github.com/user-attachments/assets/4865c999-8fd9-4f53-a70d-99edb0be9d06)

**Answer**: MD4 (can be confirmed through CrackStation website)

3. Crack hashA.txt using john the ripper, what is the password?

`echo "f9d4049dd6a4dc35d40e5265954b2a46" > hash.txt`

`john --format=raw-md4 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`

![image](https://github.com/user-attachments/assets/4b261e57-96e7-4d4b-870a-72e0892739a0)

4. What is the hash type stored in the file hashB.txt

Finding the hashB.txt `find / -type f -name hashB.txt 2>/dev/null`

![image](https://github.com/user-attachments/assets/251d996a-f9a7-4b38-a73d-cca8e1fdcfdb)

Going to the craft directory and checking the contents of hashB.txt `b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3`

Checking through CrackStation website

**Answer**: SHA-1

5. Find a wordlist  with the file extention of '.mnf' and use it to crack the hash with the filename hashC.txt. What is the password?

Finding the file of extension .mnf `find / -type f -name "*.mnf" 2>/dev/null`

![image](https://github.com/user-attachments/assets/38b0fd0f-74ad-4c5c-afdb-380ab270b516)

Finding the hashC.txt `find / -type f -name hashC.txt 2>/dev/null`

![image](https://github.com/user-attachments/assets/69938406-ed88-4299-b5df-050d6d939412)

Going to the server_mail directory and checking the contents of hashC.txt `c05e35377b5a31f428ccda9724a9dfbd0c5d71dccac691228d803c78e2e8da29`

`echo " c05e35377b5a31f428ccda9724a9dfbd0c5d71dccac691228d803c78e2e8da29" > hashC.txt`

Getting the wordlist ww.mnf in Linux machine by scp command `scp "sarah@10.10.140.81:/home/sarah/system AB/db/ww.mnf" ~/Downloads/`

![image](https://github.com/user-attachments/assets/70508429-4ec0-4360-8dab-1ea6dab9d44a)

Checking the hash of hashC.txt by hash-identifier `cat hashC.txt | hash-identifier`

![image](https://github.com/user-attachments/assets/65b8a909-2659-4b5c-9e37-cfb1b65c7851)

Cracking the hash by john the ripper, the wordlist is in my current directory `john --format=raw-sha256 --wordlist=./ww.mnf hashC.txt`

![image](https://github.com/user-attachments/assets/f3e0d569-b77d-4411-8c46-adfa9a68f3a8)

6. Crack hashB.txt using john the ripper, what is the password?

As we have already found out that it is SHA-1 hash so using john the ripper

`echo "b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3" > hashB.txt`

`john --format=raw-sha1 --wordlist=/usr/share/wordlists/rockyou.txt hashB.txt`

![image](https://github.com/user-attachments/assets/45cd11c4-9707-4094-a846-b651d460d0fe)

## Decoding base64

Base64 is a group of binary-to-text encoding schemes that represent binary data in an ASCII string format.

It is just another way in which data can be represented

There may be times when you encounter base64 converted data in files on a system and needed to convert it to a human readable format.

We can use the tool 'base64' with a pipe to translate it back to something that is human readable.

Syntax: `cat [filename] | base64 -d`

To transfer the output to a new text file simply use he > operator followed by the new filename.

Example: `cat encodedData.txt | base64 -d > new.txt`

Encoding/decoding is changing data format. The data itself does not change, just how it reads.

### Answer the questions below

1. What is the name of the tool which allows us to decode base64 strings?

base64

2. Find a file called encoded.txt. What is the special answer?

Finding the encoded.txt `find / -type f -name encoded.txt 2>/dev/null`

![image](https://github.com/user-attachments/assets/7fdf897f-5770-460c-bb43-09076475aec0)

Decoding this encoded.txt by base64 command and putting this in new file newEncoded.txt

`cat encoded.txt | base64 -d > newEncoded.txt`

Using the less command to see the decoded text

The first line says to find the special keyword `/special`

![image](https://github.com/user-attachments/assets/cc59dd72-d55c-4233-ae37-cbbbff43b40e)

Finding the ent.txt file and checking the content of file `find / -type f -name ent.txt 2>/dev/null`

![image](https://github.com/user-attachments/assets/ae2b9067-398f-4740-a1ce-d5685517ff0f)

This is a hash `bfddc35c8f9c989545119988f79ccc77`.

Checking through CrackStation website, it is md4 hash and result is john.

## Encryption/Decryption using gpg

Encryption refers to the process of concealing sensitive data by converting it to an unintelligible format. The only way to reverse the process is to use a key; this is known as decryption.

Encryption is just a way to protect data using a private key.

For example, the following string 'secret data' can be converted to `QFnvZbCSffGzrauFXx9icxsN9UHHuU+sCL0sGcUCPGKyRquc9ldAfFIpVI+m8mc/` using a key derived from the password 'pass'.

It is also important to note that there are many different types of encryption schemes, known as algorithms such as AES-256/128, 3DES, Blowfish, etc.

Among these, AES is considered to be the recommended encryption algorithm to use due to the fact that it has been tested and proven to be a strong scheme.

The Advanced Encryption Standard (AES) is a symmetric block encryption algorithm. It can use cryptographic keys of sizes 128, 192, and 256 bits.

There are two main types of encryption methods, asymmetric and symmetric.

GPG stands for GNU Privacy Guard. It is a free and open-source encryption software that uses public-key cryptography. GPG can be used to encrypt files and messages, and to sign files and messages. Encryption makes it so that only the intended recipient can decrypt the file or message while signing makes it so that the recipient can verify that the file or message was sent by the person it claims to be from.

File can be encrypted using the the program gpg to encrypt it using the AES-256 scheme:

Syntax: `gpg --cipher-algo [encryption type] [encryption method] [file to encrypt]`

It will then ask for a password to be the key to decrypt the file

Then a new encrypted file will be created with the extension gpg.

For decrypting the file

Syntax: `gpg [encrypted file]`

**Note**: You may notice how it does not ask us for the password to decrypt the file, this is because we we have already entered it when we were encrypting the file and so Linux stored the password for quick use. However if we restart our system or attempt to decrypt the file in a different linux machine, it will ask us for the password to decrypt the file.

### Answer the questions below

1. You wish to encrypt a file called history_logs.txt using the AES-128 scheme. What is the full command to do this?

`gpg --cipher-algo AES-128 --symmetric history_logs.txt`

2. What is the command to decrypt the file you just encrypted?
   
`gpg history_logs.txt.gpg`

3. Find an encrypted file called layer4.txt, its password is bob. Use this to locate the flag. What is the flag?

Finding the fie layer4.txt and going to the directory `find / -type f -name layer4.txt 2>/dev/null`

![image](https://github.com/user-attachments/assets/5d4b59a1-8d92-4f04-8f4c-d410c25f3a81)

Decrypting the layer4.txt, asks for the password, type bob and then gave a name for the filename which is decrypted.

`gpg layer4.txt`

![image](https://github.com/user-attachments/assets/0e3737c6-b4f2-4d63-9f7b-557b2614a949)

Checking the contents of layer4En.txt

![image](https://github.com/user-attachments/assets/deae8bbe-be42-44d7-b6b0-8087283c9c0b)

Finding the layer3.txt and decrypting the file

`find / -type f -name layer3.txt 2>/dev/null`

`gpg layer3.txt`

![image](https://github.com/user-attachments/assets/a7eea7e1-fca7-429c-a1b9-f2a40d5aed6d)

Finding the layer2.txt and decrypting the file

`find / -type f -name layer2.txt 2>/dev/null`

`gpg layer2.txt`

![image](https://github.com/user-attachments/assets/4dfa3829-fe10-4a9e-8cd5-5cae863e250b)

This is string encoded in base 64 `MS4gRmluZCBhIGZpbGUgY2FsbGVkIGxheWVyMS50eHQsIGl0cyBwYXNzd29yZCBpcyBoYWNrZWQu`

Decoding this through base64 command `cat layer2En.txt | base64 -d`

![image](https://github.com/user-attachments/assets/93ec47a3-dc82-4633-822b-bad37b0420d8)

Finding the layer1.txt and decrypting the file

`find / -type f -name layer1.txt 2>/dev/null`

`gpg layer1.txt`

![image](https://github.com/user-attachments/assets/ea2463e6-02cf-4c1a-85c7-b3f6914b612d)

## Cracking Encrypted gpg files

If we donot have the key or password for the encrypted files, we can brute force like the john the ripper to check every usual key for the encrypted file.

If you are using Kali linux or Parrot OS, you should have a binary add on called gpg2john.

This binary program allows us to convert the gpg file into a hash string that john the ripper can understand when it comes to brute-forcing the password against a wordlist.

To generate the hash of the encrypted file for John the Ripper

Syntax: `gpg2john [encrypted gpg file] > [filename of the hash you want to create]`

The command above allows us to generate the hash for John the Ripper to understand. 

Syntax: `john wordlist=[location/name of wordlist] --format=gpg [name of hash we just created]`

### Answer the questions below

1. Find an encrypted file called personal.txt.gpg and find a wordlist called data.txt. Use tac to reverse the wordlist before brute-forcing it against the encrypted file. What is the password to the encrypted file?

Finding the encrypted file and wordlist

`find / -type f -name personal.txt.gpg 2>/dev/null`

`find / -type f -name data.txt 2>/dev/null`

![image](https://github.com/user-attachments/assets/56f259ad-e460-4634-a072-e8f887db55ca)

Getting both files into the Linux machine

`scp "sarah@10.10.11.193://home/sarah/oldLogs/units/personal.txt.gpg" ~/Downloads`

`scp "sarah@10.10.11.193:/home/sarah/logs/zmn/old stuff/-mvLp/data.txt" ~/Downloads`

![image](https://github.com/user-attachments/assets/ddbfc9ca-b8d5-4fe2-b653-383010f1ab43)

Reversing the wordlist data.txt `tac data.txt > reversed_data.txt`

Creating the hash of the encrypted file by gpg2john `gpg2john personal.txt.gpg > hash_created`

![image](https://github.com/user-attachments/assets/7f44cab2-5ea2-459b-b8d9-bbc40b7ac038)

Cracking the hash by john the ripper `john --wordlist=./reversed_data.txt --format=gpg hash_created`

![image](https://github.com/user-attachments/assets/90a70dff-543f-473e-b78a-cb53c8b7e9ad)

3. What is written in this now decrypted file?

Decrypting the file personal.txt.gpg 

`gpg personal.txt.gpg`

This decrypts the file into personal.txt

Checking the contents of personal.txt

![image](https://github.com/user-attachments/assets/705a2e0d-5af8-40c6-b8f3-c51abf21e68f)
