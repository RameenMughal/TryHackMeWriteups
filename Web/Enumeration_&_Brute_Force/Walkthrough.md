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

<img width="836" height="227" alt="image" src="https://github.com/user-attachments/assets/3ae20550-20b1-4a17-b1ba-0fb43fbfd945" />

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

## Enumerating Users via Verbose Errors

### Understanding Verbose Errors

In the world of web development, verbose errors are like unintentional whispers of a system, revealing secrets meant to be kept hidden. These detailed error messages are invaluable during the debugging process, helping developers understand exactly what went wrong. However, just like an overheard conversation might reveal too much, these verbose errors can unintentionally expose sensitive data to those who know how to listen.

Verbose errors can turn into a goldmine of information, providing insights such as:

- **Internal Paths**: Like a map leading to hidden treasure, these reveal the file paths and directory structures of the application server which might contain configuration files or secret keys that aren't visible to a normal user.
- **Database Details**: Offering a sneak peek into the database, these errors might spill secrets like table names and column details.
- **User Information**: Sometimes, these errors can even hint at usernames or other personal data, providing clues that are crucial for further investigation.

---

### Inducing Verbose Errors

Attackers induce verbose errors as a way to force the application to reveal its secrets. Below are some common techniques used to provoke these errors:

1. **Invalid Login Attempts**: By intentionally entering incorrect usernames or passwords, attackers can trigger error messages that help distinguish between valid and invalid usernames. For example, entering a username that doesn’t exist might trigger a different error message than entering one that does, revealing which usernames are active.
2. **SQL Injection**: This technique involves slipping malicious SQL commands into entry fields, hoping the system will stumble and reveal information about its database structure. For example, placing a single quote (`'`) in a login field might cause the database to throw an error, inadvertently exposing details about its schema.
3. **File Inclusion/Path Traversal**: By manipulating file paths, attackers can attempt to access restricted files, causing the system to display errors that expose its internal file paths. For example, using directory traversal sequences like `../../` could lead to errors that disclose restricted file paths.
4. **Form Manipulation**: Changing the values in a web form can make the application show error messages that reveal how the backend works or expose sensitive information. For example, changing hidden form fields to cause validation errors may reveal what type or format of data the application expects.
5. **Application Fuzzing**: Sending unexpected inputs to various parts of the application to see how it reacts can help identify weak points. For example, tools like Burp Suite Intruder are used to automate the process, bombarding the application with varied payloads to see which ones provoke informative errors.

---

### The Role of Enumeration and Brute Forcing

When it comes to breaching authentication, enumeration and brute forcing often go hand in hand:
- **User Enumeration**: Discovering valid usernames sets the stage, reducing the guesswork in subsequent brute-force attacks.
- **Exploiting Verbose Errors**: The insights gained from these errors can illuminate aspects like password policies and account lockout mechanisms, paving the way for more effective brute-force strategies.
In summary, verbose errors are like breadcrumbs leading attackers deeper into the system, providing them with the insights needed to tailor their strategies and potentially compromise security in ways that could go undetected until it’s too late.

---

### Enumeration in Authentication Forms

In this HackerOne report [User enumeration through forget password](https://hackerone.com/reports/1166054), the attacker was able to enumerate users using the website's Forget Password function. 

Similarly, we can also enumerate emails in login forms. For example, navigate to `http://enum.thm/labs/verbose_login/` and put any email address in the Email input field.

When you input an invalid email, the website will respond with "Email does not exist." indicating that the email has not been registered yet.

<img width="851" height="168" alt="image" src="https://github.com/user-attachments/assets/b434e0a9-708f-486b-9ee2-c42be2768f02" />

However, if the email is already registered, the website will respond with an "Invalid password" error message, indicating that the email exists in the database but the password is incorrect.

<img width="850" height="178" alt="image" src="https://github.com/user-attachments/assets/c8b863bf-0522-4787-b2e9-210da3d4b2ed" />

---

### Automation

Python script is given that will check for valid emails in the target web app. Save the code below as `script.py`.

**Breakdown of the script**:

**url**: The script targets the endpoint handling the login functionality of the application.

```
url = 'http://enum.thm/labs/verbose_login/functions.php'
```







