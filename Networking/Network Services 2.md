# Network Services 2

<img width="895" height="178" alt="image" src="https://github.com/user-attachments/assets/c441ce65-5ba4-46c9-adc3-7f0122e77a86" />

## Understanding NFS

### What is NFS?

NFS stands for "Network File System" and allows a system to share directories and files with others over a network. By using NFS, users and programs can access files on remote systems almost as if they were local files.

It does this by mounting all, or a portion of a file system on a server. The portion of the file system that is mounted can be accessed by clients with whatever privileges are assigned to each file.

Mounting refers to the process of making a file system accessible at a certain point in the directory tree of a Linux operating system.

### How does NFS work?

When a client wants to access a directory from a remote host, it sends a request to mount that directory onto a local directory on its system, similar to how a physical device can be mounted. The mount service facilitates this connection by interacting with the relevant mount daemon using Remote Procedure Calls (RPC). 

The server checks if the user has permission to mount whatever directory has been requested. It will then return a file handle which uniquely identifies each file and directory that is on the server.

A daemon is a background process that runs on a computer system, typically without direct user interaction.

If someone wants to access a file using NFS, an RPC call is placed to NFSD (the NFS daemon) on the server. This call takes parameters such as:
- The file handle
- The name of the file to be accessed
- The user's, user ID
- The user's group ID

These are used in determining access rights to the specified file. This is what controls user permissions, I.E read and write of files.

### What runs NFS?

Using the NFS protocol, you can transfer files between computers running Windows and other non-Windows operating systems, such as Linux, MacOS or UNIX.

A computer running Windows Server can serve as an NFS file server, which means it can host files that can be accessed by client computers that are not running Windows, such as those using Linux, MacOS, or UNIX. This capability is essential for organizations that utilize diverse operating systems, allowing for file sharing and collaboration across different platforms. 

Furthermore, the NFS protocol enables a Windows-based computer to access files located on a non-Windows NFS server, facilitating seamless data transfer and resource sharing.

### Answer the questions below

1. What does NFS stand for?

Network File System

2. What process allows an NFS client to interact with a remote directory as though it was a physical device?

Mounting

3. What does NFS use to represent files and directories on the server?

File Handle

4. What protocol does NFS use to communicate between the server and client?

RPC

5. What two pieces of user data does the NFS server take as parameters for controlling user permissions? Format: parameter 1 / parameter 2

user id / group id

6. Can a Windows NFS server share files with a Linux client? (Y/N)

Y

7. Can a Linux NFS server share files with a MacOS client? (Y/N)

Y

8. What is the latest version of NFS? [released in 2016, but is still up to date as of 2020] This will require external research.

4.2

## Enumerating NFS

### What is Enumeration?

Enumeration is defined as "a process which establishes an active connection to the target hosts to discover potential attack vectors in the system, and the same can be used for further exploitation of the system." - Infosec Institute. 

It is a critical phase when considering how to enumerate and exploit a remote machine - as the information you will use to inform your attacks will come from this stage.

### Requirements

In order to do a more advanced enumeration of the NFS server, and shares- we're going to need a few tools. The first of which is key to interacting with any NFS share from your local machine: `nfs-common`.

### NFS-Common

It is important to have this package installed on any machine that uses NFS, either as client or server. It includes programs such as: `lockd`, `statd`, `showmount`, `nfsstat`, `gssd`, `idmapd` and `mount.nfs`. 

Primarily, we are concerned with `showmount` and `mount.nfs` as these are going to be most useful to us when it comes to extracting information from the NFS share.

You can install `nfs-common` using `sudo apt install nfs-common`, it is part of the default repositories for most Linux distributions such as the Kali Remote Machine

### Port Scanning

The first step of enumeration is to conduct a port scan, to find out as much information as you can about the services, open ports and operating system of the target machine. 

You can go as in-depth as you like on this, however, I suggest using `nmap` with the `-A` and `-p-` tags.

### Mounting NFS shares

Your client’s system needs a directory where all the content shared by the host server in the export folder can be accessed. You can create this folder anywhere on your system. 

Once you've created this mount point, you can use the `mount` command to connect the NFS share to the mount point on your machine like so: `sudo mount -t nfs IP:share /tmp/mount/ -nolock`

| Tag       | Function                                                   |
|-----------|------------------------------------------------------------|
| `sudo`    | Run the following command as root                          |
| `mount`   | Execute the mount command                                  |
| `-t nfs`  | Specify the filesystem type as NFS                         |
| `IP:share`| The NFS server IP address and the exported share name      |
| `-nolock` | Disable NLM (network lock manager) locking when mounting   |

### Answer the questions below

Run an nmap scan of your choice.

1. How many ports are open on the target machine?

7 

Running an nmap scan command nmap -p- --min-rate 1000 -T4 `MACHINE_IP`

<img width="340" height="149" alt="image" src="https://github.com/user-attachments/assets/3accaec2-aaf1-43fe-b96e-7f62afe71f4b" />

2. Which port contains the service we're looking to enumerate?

2049

3. Now, use `/usr/sbin/showmount -e [IP]` to list the NFS shares, what is the name of the visible share?

/home

<img width="197" height="35" alt="image" src="https://github.com/user-attachments/assets/63de9585-858e-4ad2-aa1e-696201d931fb" />

4. Time to mount the share to our local machine!

First, use `mkdir /tmp/mount` to create a directory on your machine to mount the share to. This is in the `/tmp` directory- so be aware that it will be removed on restart.

Then, use the mount command we broke down earlier to mount the NFS share to your local machine. Change directory to where you mounted the share- what is the name of the folder inside?

cappucino

After making the directory by `mkdir /tmp/mount`. Mounting the /home in our local machine by `sudo mount -t nfs MACHINE_IP:/home /tmp/mount/ -nolock`. Then move to the `/tmp/mount` directory by `cd` to check directories inside by `ls` command.

<img width="97" height="26" alt="image" src="https://github.com/user-attachments/assets/2fba8e5a-7ea7-43a0-87a0-352faf5cec1e" />

5. Have a look inside this directory, look at the files. Looks like  we're inside a user's home directory...

<img width="310" height="131" alt="image" src="https://github.com/user-attachments/assets/7f3d53c0-cff6-45be-ba49-a557e7f2b384" />

6. Interesting! Let's do a bit of research now, have a look through the folders. Which of these folders could contain keys that would give us remote access to the server?

`.ssh`

7. Which of these keys is most useful to us?

`id_rsa`

You can see the files in `.ssh` directory by `ls` command

8. Copy this file to a different location your local machine, and change the permissions to `600` using `chmod 600 [file]`.

Assuming we were right about what type of directory this is, we can pretty easily work out the name of the user this key corresponds to.

Can we log into the machine using ssh -i <key-file> <username>@<ip> ? (Y/N)

Y

Copy the id_rsa file to different location. As I want to copy this file in my current directory so `cp -r /tmp/mount/cappucino/.ssh/id_rsa .`

Giving permissions to `id_rsa` file by `chmod 600 id_rsa`.

Logging to the machine by `ssh -i id_rsa cappucino@MACHINE_IP`

<img width="340" height="290" alt="image" src="https://github.com/user-attachments/assets/f3d72385-7b13-47c2-8be8-6afd29c91cad" />

### Exploiting NFS

If you have a low privilege shell on any machine and you found that a machine has an NFS share you might be able to use that to escalate privileges, depending on how it is configured.

**What is root_squash?**

Remote users are assigned the user 'nfsnobody' with the least local privileges to enhance security. This practice ensures that even if a remote user connects as root, they cannot perform actions that could compromise the host system. Not what we want. However, if this is turned off, it can allow the creation of SUID bit files, allowing a remote user root access to the connected system.

**SUID**

Files with the SUID (Set User ID) bit set allow users to execute the file with the privileges of the file's owner. This means that if a file is owned by the super-user (root), any user running this file will execute it with root permissions.

**Method**

We're able to upload files to the NFS share, and control the permissions of these files. We can set the permissions of whatever we upload, in this case a bash shell executable. We can then log in through SSH, as we did in the previous task- and execute this executable to gain a root shell!

**The Executable**

Due to compatibility reasons,  we will obtain the bash executable directly from the target machine.
With the key obtained in the previous task, we can use SCP with the command `scp -i key_name username@MACHINE_IP:/bin/bash ~/Downloads/bash` to download it onto our attacking machine.

Another method to overcome compatibility issues is to obtain a standard Ubuntu Server 18.04 bash executable, the same as the server's- as we know from our nmap scan. You can download it [here](https://github.com/polo-sec/writing/blob/master/Security%20Challenge%20Walkthroughs/Networks%202/bash). If you want to download it via the command line, be careful not to download the github page instead of the raw script. You can use `wget https://github.com/polo-sec/writing/raw/master/Security%20Challenge%20Walkthroughs/Networks%202/bash`. 

**Mapped Out Pathway:**

If this is still hard to follow, here's a step by step of the actions we're taking, and how they all tie together to allow us to gain a root shell:

NFS Access -> Gain Low Privilege Shell -> Upload Bash Executable to the NFS share -> Set SUID Permissions Through NFS Due To Misconfigured Root Squash -> Login through SSH -> Execute SUID Bit Bash Executable -> ROOT ACCESS

## Understanding SMTP

**What is SMTP?**

SMTP stands for "Simple Mail Transfer Protocol". It is utilised to handle the sending of emails. In order to support email services, a protocol pair is required, comprising of SMTP and POP/IMAP. Together they allow the user to send outgoing mail and retrieve incoming mail, respectively.

The SMTP server performs three basic functions:
- It verifies who is sending emails through the SMTP server.
- It sends the outgoing mail
- If the outgoing mail can't be delivered it sends the message back to the sender

Most people will have encountered SMTP when configuring a new email address on some third-party email clients, such as Thunderbird; as when you configure a new email client, you will need to configure the SMTP server configuration in order to send outgoing emails.

A third-party email client is a program that helps you send and receive emails using your email account from a different company than your email provider. For example, if you have a Gmail account, you can use a third-party email client like Microsoft Outlook to check your emails instead of using the Gmail website. These clients often have extra features for organizing your emails and managing multiple accounts in one place.

**POP and IMAP**

POP (Post Office Protocol) and IMAP (Internet Message Access Protocol) are two protocols used for retrieving email from a mail server. POP downloads emails from the server to the user's device and typically removes them from the server, allowing offline access to messages. IMAP, on the other hand, keeps emails on the server, enabling users to access their messages from multiple devices while maintaining synchronization. 

**How does SMTP work?**

Email delivery functions much the same as the physical mail delivery system. The user will supply the email (a letter) and a service (the postal delivery service), and through a series of steps- will deliver it to the recipients inbox (postbox). 

The role of the SMTP server in this service, is to act as the sorting office, the email (letter) is picked up and sent to this server, which then directs it to the recipient.

We can map the journey of an email from your computer to the recipient’s like this:

<img width="1042" height="519" alt="image" src="https://github.com/user-attachments/assets/4e9f117a-fafc-439b-a51b-a3c928294526" />

1. The mail user agent, which is either your email client or an external program. connects to the SMTP server of your domain, e.g. smtp.google.com. This initiates the SMTP handshake. This connection works over the SMTP port- which is usually 25. Once these connections have been made and validated, the SMTP session starts.

2. The process of sending mail can now begin. The client first submits the sender, and recipient's email address- the body of the email and any attachments, to the server.

3. The SMTP server then checks whether the domain name of the recipient and the sender is the same.

4. The SMTP server of the sender will make a connection to the recipient's SMTP server before relaying the email. If the recipient's server can't be accessed, or is not available- the Email gets put into an SMTP queue.

5. Then, the recipient's SMTP server will verify the incoming email. It does this by checking if the domain and user name have been recognised. The server will then forward the email to the POP or IMAP server, as shown in the diagram above.

6. The E-Mail will then show up in the recipient's inbox.

If the domain name of the recipient and the sender is not the same, the SMTP server may still allow the email to be sent, but it will depend on the server's configuration and policies. The server will check for proper authentication and may require the sender to verify their identity.

This is a very simplified version of the process, and there are a lot of sub-protocols, communications and details that haven't been included. 

**What runs SMTP?**

SMTP Server software is readily available on Windows server platforms, with many other variants of SMTP being available to run on Linux.

### Answer the questions below

1. What does SMTP stand for?

Simple Mail Transfer Protocol

2. What does SMTP handle the sending of? (answer in plural)

Emails

3. What is the first step in the SMTP process?

SMTP Hnadshake

4. What is the default SMTP port?

25

5. Where does the SMTP server send the email if the recipient's server is not available?

SMTP Queue

6. On what server does the Email ultimately end up on?

POP/IMAP

7. Can a Linux machine run an SMTP server? (Y/N)

Y

8. Can a Windows machine run an SMTP server? (Y/N)

Y














