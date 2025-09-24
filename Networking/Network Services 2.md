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













