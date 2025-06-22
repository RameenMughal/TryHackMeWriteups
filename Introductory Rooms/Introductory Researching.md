# Introductory Researching

## Example Research Question

Search “hiding things inside images” on browser.

This technique is known as the Stenography and can find the document by this link [NullByte](https://null-byte.wonderhowto.com/how-to/steganography-hide-secret-data-inside-image-audio-file-seconds-0180936/)

Stenography can be done by Steghide a simple command line tool.

The simple easy technique for Stenography is the least significant bit, commonly known as LSB.

This technique changes the last few bits in a byte to encode a message, which is especially useful in something like an image, where the red, green, and blue values of each pixel are represented by eight bits (one byte) ranging from 0 to 255 in decimal or 00000000 to 11111111 in binary.

Changing the last two bits in a completely red pixel from 11111111 to 11111101 only changes the red value from 255 to 253, which to the naked eye creates a nearly imperceptible change in color but still allows us to encode data inside of the picture.

The least significant bit technique works well for media files, where slightly changing byte values creates only slight imperceptible changes, but not so well for things like ASCII text, where a single bit out of place will completely change the character. 

### Step 1: Embed Hidden Data into A File

`apt-get install steghide`

`steghide embed -ef secretFile -cf coverFile -sf outputFile -z compressionLevel -e scheme`

The arguments are broken down as follows:

•	-ef specifies the path of the file that you want to hide. You can embed any kind of file inside of the cover file, including Python scripts or shell files.

•	-cf is the file that the data is embedded into. This is restricted to BMP, JPEG, WAV, and AU files.

•	-sf is an optional argument that specifies the output file. If this is omitted, the original cover file will be overwritten by your new steganographic file.

•	-z specifies the compression level, between 1 and 9. If you prefer not to compress your file, use the argument -Z instead.

•	-e specifies the type of encryption. Steghide supports a multitude of encryption schemes, and if this argument is omitted by default, Steghide will use 128-bit AES encryption. If you prefer not use encryption, simply type -e none.

Once you have executed the Steghide command, you will be prompted to set a password that will allow you to extract the embedded data later. So enter your passphrase and re-enter it to confirm. 

### Step 2: Extract Hidden Data From the File

`$ steghide extract -sf stegoFile -xf outputFile`

Once you run this command, you'll be prompted to enter the same password you created above in order to create the extracted file.

So now we know how stenography works, search ‘extract file from jpeg stenography”

Head to the first link [0xrick](https://0xrick.github.io/lists/stego/)

One thing that it says that it can be installed by the `apt` command

Search “what is apt install”

`apt install` is a command-line tool used in Debian-based Linux distributions like Ubuntu and Linux Mint to install software packages from the system's repositories. It's part of the Advanced Package Tool (APT), which manages software packages on these systems. 

So how do we install packages through apt?

Search “how to install things with apt”

To install things from APT, you'll need to use the terminal and the apt command. First, you need to make sure your package lists are updated using sudo apt update. Then, you can install a package by using sudo apt install <package-name>, replacing <package-name> with the name of the package you want to install. 

From the “Extract file from jpeg stenography” first link, there was a useful command for extracting:

`steghide extract -sf file` : extracts embedded data from a file

Our research has been completed!

### Answer the questions below

1. In the Burp Suite Program that ships with Kali Linux, what mode would you use to manually send a request (often repeating a captured request numerous times)?

Search “Manually send request in Burp Suite"

In Burp Suite (as included in Kali Linux), the mode used to manually send a request, often repeating it numerous times, is called "Repeater".

2. What hash format are modern Windows login passwords stored in?

Search “Hash formats in Windows login passwords”

NTLM – New Technology LAN Manager

NTLM hashes use MD4 to hash the user's password in Unicode (UTF-16LE).

3. What are automated tasks called in Linux?

Search “Automated tasks in Linux”

A cron job is a scheduled task that runs automatically at specified intervals using the cron daemon (crond), which is a time-based job scheduler in Unix-like operating systems.

4. What number base could you use as a shorthand for base 2 (binary)?

Search “Shorthand number base for binary”

Hexidecimal is used extensively as a shorthand for binary. Because it is base 16 with 16 being a power of 2, conversion from binary to hex is clean.

5. If a password hash starts with $6$, what format is it (Unix variant)?

Search “Hash format of $6$”

SHA-512 Crypt format

## Vulnerability Searching 

To exploit a software for its vulnerability, there are websites like

1. [ExploitDB](https://www.exploit-db.com/)
2. [NVD](https://nvd.nist.gov/vuln/search)
3. [CVE Mitre](https://cve.mitre.org/)

NVD keeps track of CVEs (Common Vulnerabilities and Exposures) -- whether or not there is an exploit publicly available.

Common Vulnerabilities and Exposures (CVE), this term is given to a publicly disclosed vulnerability

CVEs take the form: CVE-YEAR-IDNUMBER

ExploitDB contains exploit for the vulnerability, useful for hackers.

You can also search ExploitDB from your own Linux through searchsploit.


From the example website, the software and version of the website is Fuel CMS version 1.4

To search about the vulnerability of this sotware

`searchsploit fuel cms`

Which results in the Remote Code Execution exploit we can use against this website.

CVE Numbers are assigned when it is discovered, not when it is published.

### Answer the questions below

1. What is the CVE for the 2020 Cross-Site Scripting (XSS) vulnerability found in WPForms?
   
Search in ExploitDB “Cross-Site Scripting WPForms”

CVE-2020-10385

2. There was a Local Privilege Escalation vulnerability found in the Debian version of Apache Tomcat, back in 2016. What's the CVE for this vulnerability?

Search in ExploitDB “Local Privilege Escalation Debian Apache”

CVE-2016-1240

3. What is the very first CVE found in the VLC media player?

Search in ExploitDB “VLC Media Player”, Go to the end 
CVE-2007-0017

4. If you wanted to exploit a 2020 buffer overflow in the sudo program, which CVE would you use?

Search in ExploitDB “Buffer overflow sudo”

CVE-2019-18634

## Manual Pages

`man` command – gives you access to the manual pages of tools inside your terminal.

Example: `man ssh` – gives description about the tool ssh

Syntax for the shh is `[user@]hostname` or `ssh://[user@]hostname[:port]`

We can see from the manual page that -V can be used to check the version of ssh `ssh -V`

If we want to search without checking the manual page, we can do this by adding the grep command which checks for that text in the manual page.

`man ssh | grep -e "version number"`

### Answer the questions below

1. SCP is a tool used to copy files from one computer to another.
What switch would you use to copy an entire directory?

`man scp`

`-r` Recursively copy the entire directories

2. fdisk is a command used to view and alter the partitioning scheme used on your hard drive.
What switch would you use to list the current partitions?

`man fdisk`

`-l` List the partitions of current disk

4. nano is an easy-to-use text editor for Linux. There are arguably better editors (Vim, being the obvious choice); however, nano is a great one to start with.
What switch would you use to make a backup when opening a file with nano?

`man nano`

`-B` Backup the file when editing a file

6. Netcat is a basic tool used to manually send and receive network requests. 
What command would you use to start netcat in listen mode, using port 12345?

`man netcat`

Syntax as `nc -l -p port [-options] [hostname] [port]`

`nc -l -p 1234`
