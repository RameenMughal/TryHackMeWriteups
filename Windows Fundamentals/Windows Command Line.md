# Windows Command Line

## Introduction

You can use the SSH client on the AttackBox to connect to `MACHINE_IP` with the following credentials:

Username: `user`

Password: `Tryhackme123!`

### Answer the questions below

What is the default command line interpreter in the Windows environment?

cmd.exe

## Basic System Information

Before issuing commands, we should note that we can only issue the commands within the Windows Path. You can issue the command `set` to check your path from the command line. 

The terminal output below shows the path where MS Windows will execute commands, as indicated by the line starting with `Path=`.

<img width="404" height="215" alt="image" src="https://github.com/user-attachments/assets/6e2a23de-7e1a-4ab7-ba53-d7227a9f9975" />

Let’s use the `ver` command to determine the operating system (OS) version. 

<img width="215" height="53" alt="image" src="https://github.com/user-attachments/assets/61a86557-83a6-41f1-9cbf-1b02793edd20" />

We can run the systeminfo command to list various information about the system such as OS information, system details, processor and memory.

<img width="315" height="156" alt="image" src="https://github.com/user-attachments/assets/c8379c57-ef3a-4a5d-838e-d0123f547714" />

Before moving on, it is good to mention a couple of tricks.

First, you can pipe it through more if the output is too long. Then, you can view it page after page by pressing the space bar button. 

To demonstrate this, try running `driverquery` and compare it with running `driverquery | more`

In the latter, you can display the output page by page and you can exit it using `CTRL + C`.

### Answer the questions below

1. What is the OS version of the Windows VM?

By using the `ver` command.

**Answer**: 10.0.20348.2655

2. What is the hostname of the Windows VM?

By using the `systeminfo` command, you see Host Name first

**Answer**: WINSRV2022-CORE

## Network Troubleshooting

### Network Configuration

You can check your network information using `ipconfig`. The terminal output below shows our IP address, subnet mask, and default gateway.

<img width="310" height="139" alt="image" src="https://github.com/user-attachments/assets/7975b7da-2b79-4d08-8302-d98af8c406c1" />

You can also use `ipconfig /all` for more information about your network configuration. As shown in the terminal below, we can view our DNS servers and confirm that DHCP is enabled.

<img width="378" height="312" alt="image" src="https://github.com/user-attachments/assets/d90be907-52df-4d15-9fdf-1083994678f5" />

### Network Troubleshooting

One common troubleshooting task is checking if the server can access a particular server on the Internet. The command syntax is `ping target_name`. Inspired by ping-pong, we send a specific ICMP packet and listen for a response. If a response is received, we know that we can reach the target and that the target can reach us.

Another valuable tool for troubleshooting is `tracert`, which stands for trace route. The command `tracert target_name` traces the network route traversed to reach the target. Without getting into more details, it expects the routers on the path to notify us if they drop a packet because its time-to-live (TTL) has reached zero. 

### More Networking Commands

One networking command worth knowing is `nslookup`. It looks up a host or domain and returns its IP address. The syntax `nslookup example.com` will look up `example.com` using the default name server; however, `nslookup example.com 1.1.1.1` will use the name server `one.one.one.one`

<img width="262" height="203" alt="image" src="https://github.com/user-attachments/assets/4d8b80bd-361b-42f2-adc2-853a7dedddeb" />

The final networking command we will cover in this room is `netstat`. This command displays current network connections and listening ports. A basic `netstat` command with no arguments will show you established connections

<img width="320" height="66" alt="image" src="https://github.com/user-attachments/assets/837d1e68-0ec3-408b-bd2f-bf716a189791" />

If you are curious about the other options, you can run `netstat -h`, where `-h` displays the help page. We opted for the following options:
- `-a` - displays all established connections and listening ports
- `-b` - shows the program associated with each listening port and established connection
- `-o` - reveals the process ID (PID) associated with the connection
- `-n` - uses a numerical form for addresses and port numbers

We combine these four options and execute the `netstat -abon` command. The result is quite long, but we display the first few lines in the terminal below. 

It is clear now that the executable `sshd.exe` is responsible for listening for incoming connections on port 22, as shown in the first line. We can also see the process ID (PID) associated with each connection.

<img width="377" height="162" alt="image" src="https://github.com/user-attachments/assets/4cc20934-3ec3-4409-a357-cfdaa6f4ab3c" />

### Answer the questions below

1. Which command can we use to look up the server’s physical address (MAC address)?

`ipconfig/all`

2. What is the name of the process listening on port 3389?

TermService

3. What is the subnet mask?

`255.255.0.0`

## File and Disk Management

### Working with Directories

You can use `cd` without parameters to display the current drive and directory. It is the equivalent of asking the system, where am I?

You can view the child directories using `dir`.

<img width="245" height="236" alt="image" src="https://github.com/user-attachments/assets/d7fcb172-a909-4163-b86a-ebbf6bc90c93" />

Note that you can use the following options with `dir`:
- `dir /a` - Displays hidden and system files as well.
- `dir /s` - Displays files in the current directory and all subdirectories.

You can type `tree` to visually represent the child directories and subdirectories.

<img width="223" height="148" alt="image" src="https://github.com/user-attachments/assets/04070e01-c2bf-48dc-b6a5-2ad8648b387c" />

You can change to any directory by using the command `cd target_directory`; this is equivalent to double-clicking the target_directory on your desktop. Furthermore, you can use `cd ..` to go up one level.

To create a directory, use `mkdir directory_name`; `mkdir` stands for make directory. To delete a directory, use `rmdir directory_name`; `rmdir` stands for remove directory.

### Working with Files

You can easily view text files with the command `type`. This command will dump the contents of the text file on the screen; this is convenient for files that fit within your terminal window. 

You might want to consider more for longer text files. This command will display enough text file contents to fill your terminal window. In other words, for long text files, `more` will display a single page and wait for you to press Spacebar to move by one page (flip the page) or Enter to move by one line.

The `copy` command allows you to copy files from one location to another. Example: `copy test.txt test2.txt`

It copies the contents of `test.txt` to `test2.txt`

You can move files using the `move` command. Example: `move test2.txt ..`

It moves the file in one level up directory

We can delete a file using `del` or `erase`. Example: `del test2.txt`

We can use the wildcard character * to refer to multiple files. For example, `copy *.md C:\Markdown` will copy all files with the extension `md` to the directory `C:\Markdown`.

### Answer the questions below

What are the file’s contents in C:\Treasure\Hunt?

Go to the directory `Hunt` where consist the `flag.txt` and by `type` command see the text

<img width="260" height="254" alt="image" src="https://github.com/user-attachments/assets/4ad40981-11a9-4d32-9f8b-511f4f58eb6c" />

## Task and Process Management

We can list the running processes using `tasklist`

<img width="359" height="238" alt="image" src="https://github.com/user-attachments/assets/9fc62621-f50f-48ac-90f5-3c460da0c893" />

Some filtering is helpful because the output is expected to be very long. You can check all available filters by displaying the help page using `tasklist /?`

Let’s say that we want to search for tasks related to `sshd.exe`, we can do that with the command `tasklist /FI "imagename eq sshd.exe"`. Note that `/FI` is used to set the filter image name equals `sshd.exe`.

<img width="358" height="96" alt="image" src="https://github.com/user-attachments/assets/76fb4e33-2374-43bb-aa33-cdf5f65f6f23" />

With the process ID (PID) known, we can terminate any task using `taskkill /PID target_pid`. For example, if we want to kill the process with PID 4567, we would issue the command `taskkill /PID 4567`.

### Answer the questions below

1. What command would you use to find the running processes related to notepad.exe?

`tasklist /FI "imagename eq notepad.exe"`

2. What command can you use to kill the process with PID 1516?

`taskkill /PID 1516`

## Conclusion

We intentionally omitted a few common commands as we didn’t see a real value for including them in a beginner room. 

We mention them below so that you know that the command line can be used for other tasks.
- `chkdsk`: checks the file system and disk volumes for errors and bad sectors.
- `driverquery`: displays a list of installed device drivers.
- `sfc /scannow`: scans system files for corruption and repairs them if possible.

It is equally important to know that `/?` can be used with most commands to display a help page.

In this room, we used the command `more` in two ways:
- Display text files: `more file.txt`
- Pipe long output to view it page by page: `some_command | more`

### Answer the questions below

1. The command `shutdown /s` can shut down a system. What is the command you can use to restart a system?

`shutdown /r`

2. What command can you use to abort a scheduled system shutdown?

`shutdown /a`








