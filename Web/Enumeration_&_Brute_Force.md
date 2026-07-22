# Enumeration & Brute Force

Room: [Enumeration & Brute Force](https://tryhackme.com/room/enumerationbruteforce)

Pre-requisites:
1. [Burp Suite Module](https://tryhackme.com/module/learn-burp-suite)
2. [Linux Fundamentals Module](https://tryhackme.com/module/linux-fundamentals)

<img width="937" height="206" alt="image" src="https://github.com/user-attachments/assets/81e0d097-eeb4-4784-9748-21e6e7b6217e" />

## Introduction

Authentication enumeration is a fundamental aspect of security testing, concentrating specifically on the mechanisms that protect sensitive aspects of web applications; this process involves methodically inspecting various authentication components ranging from username validation to password policies and session management. Each of these elements is meticulously tested because they represent potential vulnerabilities that, if exploited, could lead to significant security breaches.

---

### Pre-requisites

Before starting this room, you should have a basic understanding of the following concepts:
- Familiarity with HTTP and HTTPS, including request/response structures and common status codes.
- Experience using tools like Burp Suite.
- Basic proficiency in navigating and using the Linux command line.

---

### Answer the questions below

Deploy the target VM attached to this task by pressing the green Start Lab Machine button. After obtaining the machine's generated IP address, you can either use the AttackBox or your own VM connected to TryHackMe's VPN.

I am using my Kali Linux Machine, so you can check [OpenVPN](https://tryhackme.com/room/openvpn) room to connect to the TryHackMe Server. Connect by command: `sudo openvpn FILENAME`

Add `TARGET_IP` to your `/etc/hosts` file. For example:

```
TARGET_IP    enum.thm
```

Write command `sudo nano /etc/hosts` to open the file and then copy paste `TARGET_IP` and `enum.thm` there.

<img width="270" height="80" alt="image" src="https://github.com/user-attachments/assets/21fcf890-05b0-4fb1-a4bd-78cde0769803" />

After 3 minutes, visit `http://enum.thm` to access the machine.

## Authentication Enumeration

Think of yourself as a digital detective. It's not just about picking up clues—it's about understanding what these clues reveal about the security of a system. This is essentially what authentication enumeration involves. It's like piecing together a puzzle rather than just ticking off items on a checklist.

**Identifying Valid Usernames**

Knowing a valid username lets an attacker focus just on the password. You can figure out usernames in different ways, like observing how the application responds during login or password resets. For example, error messages that specify "this account doesn't exist" or "incorrect password" can hint at valid usernames, making an attacker's job easier.

**Password Policies**

The guidelines when creating passwords can provide valuable insights into the complexity of the passwords used in an application. By understanding these password rules, an attacker can guess how strong or weak the passwords are and choose the best way to crack them.

For example, the below PHP code uses regex to require a password that includes symbols, numbers, and uppercase letters:

```
<?php
$password = $_POST['pass']; // Example1
$pattern = '/^(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).+$/';

if (preg_match($pattern, $password)) {
    echo "Password is valid.";
} else {
    echo "Password is invalid. It must contain at least one uppercase letter, one number, and one symbol.";
}
?>
```

In the above example, if the supplied password doesn't satisfy the policy defined in the pattern variable, the application will return an error message revealing the regex code requirement. An attacker might generate a dictionary that satisfies this policy.

---

### Common Places to Enumerate

**Registration Pages**

Web applications typically make the user registration process straightforward and informative by immediately indicating whether an email or username is available. While this feedback is designed to enhance user experience, it can inadvertently serve a dual purpose. 

If a registration attempt results in a message stating that a username or email is already taken, the application is unwittingly confirming its existence to anyone trying to register. Attackers exploit this feature by testing potential usernames or emails, thus compiling a list of active users without needing direct access to the underlying database.

**Password Reset Features**

Password reset mechanisms are designed to help users regain access to their accounts by entering their details to receive reset instructions. However, the differences in the application's response can unintentionally reveal sensitive information. For example, variations in an application's feedback about whether a username exists can help attackers verify user identities. By analyzing these responses, attackers can refine their lists of valid usernames, substantially improving the effectiveness of subsequent attacks.

**Verbose Errors**

Verbose error messages during login attempts or other interactive processes can reveal too much. When these messages differentiate between "username not found" and "incorrect password," they're intended to help users understand their login issues. However, they also provide attackers with definitive clues about valid usernames, which can be exploited for more targeted attacks.

**Data Breach Information**

Data from previous security breaches is a goldmine for attackers as it allows them to test whether compromised usernames and passwords are reused across different platforms. If an attacker finds a match, it suggests not only that the username is reused but also potential password recycling, especially if the platform has been breached before. This technique demonstrates how the effects of a single data breach can ripple through multiple platforms, exploiting the connections between various online identities.

---

### Answer the questions below

What type of error messages can unintentionally provide attackers with confirmation of valid usernames?

Verbose Errors

