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



