# Hydra

Room: [Hydra](https://tryhackme.com/room/hydra)

<img width="944" height="194" alt="image" src="https://github.com/user-attachments/assets/f17114c3-22b2-4501-a4c8-e6892c168ae6" />

## Hydra Introduction

Hydra is a brute force online password cracking program, a quick system login password “hacking” tool.

Hydra can run through a list and “brute force” some authentication services. Imagine trying to manually guess someone’s password on a particular service (SSH, Web Application Form, FTP or SNMP) - we can use Hydra to run through a password list and speed this process up for us, determining the correct password.

It's official GitHub Repository: [Hydra GitHub Repo](https://github.com/vanhauser-thc/thc-hydra)

For more information about options and protocols used in Hydra: [Kali Hydra Tool](https://en.kali.tools/?p=220)

This shows the importance of using a strong password; if your password is common, doesn’t contain special characters and is not above eight characters, it will be prone to be guessed. A one-hundred-million-password list contains common passwords, so when an out-of-the-box application uses an easy password to log in, change it from the default! CCTV cameras and web frameworks often use `admin:password` as the default login credentials, which is obviously not strong enough.

## Using Hydra

Start the Lab Machine and your AttackBox or your own Kali Linux Machine. I will use my Kali Linux Machine to attack the Lab Machine.

If using your own Machine then connect to the TryHackMe server by `sudo openvpn <filename>`, You can refer to the [OpenVPN](https://tryhackme.com/room/openvpn) room to know how to connect through OpenVPN

You can install Hydra on an Ubuntu or Fedora system by executing `apt install hydra` or `dnf install hydra`. Furthermore, you can download it from its official [Hydra repository](https://github.com/vanhauser-thc/thc-hydra).

---

### Hydra Commands

The options we pass into Hydra depend on which service (protocol) we’re attacking. 

For example, if we wanted to brute force FTP with the username being `user` and a password list being `passlist.txt`, we’d use the following command: 

`hydra -l user -P passlist.txt ftp://TARGET_IP`

For this deployed machine, here are the commands to use Hydra on SSH and a web form (POST method).

#### SSH

`hydra -l <username> -P <full path to pass> TARGET_IP -t 4 ssh`

<img width="896" height="206" alt="image" src="https://github.com/user-attachments/assets/e3e39b4c-109c-424a-a9bb-090887e63380" />

In Hydra, threads are the number of simultaneous login attempts Hydra performs at the same time.

`-t 4` tells Hydra to use 4 parallel threads, so it can test 4 passwords at once.

For example, `hydra -l root -P passwords.txt TARGET_IP -t 4 ssh` will run with the following arguments:
- Hydra will use `root` as the username for ssh
- It will try the passwords in the `passwords.txt` file
- There will be four threads running in parallel as indicated by `-t 4`

#### Post Web Form

We can use Hydra to brute force web forms, too. You must know which type of request it is making; GET or POST methods are commonly used. You can use your browser’s network tab (in developer tools) to see the request types or view the source code.

`sudo hydra <username> <wordlist> TARGET_IP http-post-form "<path>:<login_credentials>:<invalid_response>"`

<img width="842" height="356" alt="image" src="https://github.com/user-attachments/assets/0dfc9c20-30e1-47cc-9545-0f51240c7816" />

Below is a more concrete example Hydra command to brute force a POST login form: 

`hydra -l <username> -P <wordlist> TARGET_IP http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -V`

- The login page is only `/`, i.e., the main IP address.
- The `username` is the form field where the username is entered
- The specified username(s) will replace `^USER^`
- The `password` is the form field where the password is entered
- The provided passwords will be replacing `^PASS^`
- Finally, `F=incorrect` is a string that appears in the server reply when the login fails

On a side note, if the web server is listening on a non-default port number, you can explicitly specify the port number using `-s <port>`, for example:

`hydra -l <username> -P <wordlist> TARGET_IP http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -s <port> -V`

---

### Answer the questions below

1. Use Hydra to brute-force molly's web password. What is the value of flag 1?

Checking the web page on broswer `http://TARGET_IP` redirects to `http://TARGET_IP/login`: 

<img width="847" height="334" alt="image" src="https://github.com/user-attachments/assets/1e1e4ba1-200b-4e28-85bf-07d6b6ed374f" />

Command: `hydra -l molly -P /usr/share/wordlists/rockyou.txt TARGET_IP http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" -V`

We get the password of username `molly` that is `sunshine`:

<img width="506" height="202" alt="image" src="https://github.com/user-attachments/assets/78a17bca-1ff4-4b56-8e95-6b7a3afc7cb4" />

Fill the Username and Password in Web Login and we get the Flag1!

<img width="1692" height="661" alt="image" src="https://github.com/user-attachments/assets/0717ece0-2c04-4e92-85f7-6276c4d8be5e" />

2. Use Hydra to brute-force molly's SSH password. What is the value of flag 2?

Command: `hydra -l molly -P /usr/share/wordlists/rockyou.txt -t 4 ssh://TARGET_IP -V`

<img width="506" height="211" alt="image" src="https://github.com/user-attachments/assets/66ac7d45-d156-4014-a8dd-7730aec45a18" />

Now login via SSH: `ssh molly@TARGET_IP` and write the password, we logged in Molly's machine:

<img width="599" height="238" alt="image" src="https://github.com/user-attachments/assets/1fc22d75-eea0-4283-999b-dc1028756734" />

Use the `ls` and `cat` commands to see the flag2:

<img width="553" height="151" alt="image" src="https://github.com/user-attachments/assets/6aa1a86b-2731-4776-8ad7-fa107b20e4ca" />










