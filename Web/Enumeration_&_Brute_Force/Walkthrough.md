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

**How do you know that it is `functions.php`?**: By clicking "View Page Source", you can see html code of the web page, wher in the end you can see `script.js`, by opening this you can see the code that it manages the login feature.

It takes the data and sends to the `functions.php` to check if the login is successful or failed.

**headers**: A collection of HTTP headers is defined to mimic a typical browser request, ensuring the requests appear legitimate

```
headers = {
      'Host': 'enum.thm',
      'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'X-Requested-With': 'XMLHttpRequest',
      'Origin': 'http://enum.thm',
      'Connection': 'close',
      'Referer': 'http://enum.thm/labs/verbose_login/',
  }
```

**Main Loop**: The script reads email addresses from a provided file and checks each for validity using the check_email function.

```
for email in email_list:
    check_email(email)
```

**Crafting and Sending HTTP Requests**: For each email, the script constructs a data dictionary that includes the email address, a placeholder password, and a command to execute the 'login' function.

```
data = {'username': email, 'password': 'password', 'action': 'login'}
response = requests.post(url, headers=headers, data=data)
```

We can use a common list of emails from this repository [Gmail Usernames](https://github.com/nyxgeek/username-lists/blob/master/usernames-top100/usernames_gmail.com.txt).

Once you've downloaded the payload list, use the script on your own machine to check for valid email addresses.

Command: `python3 script.py usernames_gmail.com.txt`

<img width="334" height="205" alt="image" src="https://github.com/user-attachments/assets/28e8cb5b-54e9-4039-9c74-10298f3bcce6" />

---

### Answer the questions below

What is the valid email address from the list?

`canderson@gmail.com`

<img width="185" height="140" alt="image" src="https://github.com/user-attachments/assets/11f287ee-cebf-49ed-9db6-e41632814b1a" />

## Exploiting Vulnerable Password Reset Logic

### Password Reset Flow Vulnerabilities

Password reset mechanism is an important part of user convenience in modern web applications. However, their implementation requires careful security considerations because poorly secured password reset processes can be easily exploited.

**Email-Based Reset**

When a user resets their password, the application sends an email containing a reset link or a token to the user’s registered email address. The user then clicks on this link, which directs them to a page where they can enter a new password and confirm it, or a system will automatically generate a new password for the user. This method relies heavily on the security of the user's email account and the secrecy of the link or token sent.

**Security Question-Based Reset**

This involves the user answering a series of pre-configured security questions they had set up when creating their account. If the answers are correct, the system allows the user to proceed with resetting their password. While this method adds a layer of security by requiring information only the user should know, it can be compromised if an attacker gains access to personally identifiable information (PII), which can sometimes be easily found or guessed.

Each of these methods has its vulnerabilities:

- **Predictable Tokens**: If the reset tokens used in links or SMS messages are predictable or follow a sequential pattern, attackers might guess or brute-force their way to generate valid reset URLs.
- **Token Expiration Issues**: Tokens that remain valid for too long or do not expire immediately after use provide a window of opportunity for attackers. It’s crucial that tokens expire swiftly to limit this window.
- **Insufficient Validation**: The mechanisms for verifying a user’s identity, like security questions or email-based authentication, might be weak and susceptible to exploitation if the questions are too common or the email account is compromised.
- **Information Disclosure**: Any error message that specifies whether an email address or username is registered can inadvertently help attackers in their enumeration efforts, confirming the existence of accounts.
- **Insecure Transport**: The transmission of reset links or tokens over non-HTTPS connections can expose these critical elements to interception by network eavesdroppers.

---

### Exploiting Predictable Tokens

Tokens that are simple, predictable, or have long expiration times can be particularly vulnerable to interception or brute force. For example, the below code is used by the vulnerable application hosted in the Predictable Tokens lab:

```
$token = mt_rand(100, 200);
$query = $conn->prepare("UPDATE users SET reset_token = ? WHERE email = ?");
$query->bind_param("ss", $token, $email);
$query->execute();
```

The code above sets a random three-digit PIN as the reset token of the submitted email. Since this token doesn't employ mixed characters, it can be easily brute-forced.

To demonstrate this, go to `http://enum.thm/labs/predictable_tokens/`.

<img width="833" height="169" alt="image" src="https://github.com/user-attachments/assets/7314f5ff-7c87-43b1-ac09-950536a8d6b7" />

Navigate to the application's password reset page, input "admin@admin.com" in the Email input field, and click Submit.

The application will respond with a success message.

<img width="545" height="178" alt="image" src="https://github.com/user-attachments/assets/6ffebb27-09a7-46f5-8103-b4c7e1c2d0d4" />

For demonstration purposes, the web application uses the reset link: `http://enum.thm/labs/predictable_tokens/reset_password.php?token=123`

<img width="512" height="162" alt="image" src="https://github.com/user-attachments/assets/7dea516d-7e57-407b-b712-637164ccd935" />

Notice the token is a simple numeric value. Using Burp Suite, navigate to the above URL and capture the request.

First from the "Proxy" section, capture the request and then check the request from the subsection of Proxy "HTTP History":

<img width="629" height="352" alt="image" src="https://github.com/user-attachments/assets/4fd05e64-b945-4bee-8c1e-414621cfcfbf" />

Subsequently, send the request to the Intruder, highlight the value of the token parameter, and click the Add payload button, as shown below.

First highlight the "123" and then click the button "Add" so the payload section will open.

<img width="781" height="190" alt="image" src="https://github.com/user-attachments/assets/b3c0534d-3dd2-4601-ba18-ca5a4ccab267" />

Using the AttackBox or your own attacking VM, use Crunch to generate a list of numbers from 100 to 200. This list will be used as the dictionary in the brute-force attack.

Command: `crunch 3 3 -o otp.txt -t %%% -s 100 -e 200 `

<img width="334" height="98" alt="image" src="https://github.com/user-attachments/assets/eb8b1c97-9771-4030-932c-60db27868e8b" />

Go back to Intruder and configure the payload to use the generated file.

<img width="2986" height="1380" alt="image" src="https://github.com/user-attachments/assets/76673e3f-e942-4353-b31a-c49810e74392" />

<img width="2720" height="824" alt="image" src="https://github.com/user-attachments/assets/f910ef31-eec1-4c15-889c-1cbcfca7ee93" />

Click the "Start Attack" Button.

The attack will take some time to finish if you're using Burp Suite Community Edition. However, once successful, you will get a response with a much bigger content length compared to the responses with an "Invalid token" error message.

<img width="577" height="335" alt="image" src="https://github.com/user-attachments/assets/1a0a7f08-5a56-4a2e-922a-d1266dd528cd" />

Log in to the application using the new password.

---

### Answer the questions below

What is the flag?

<img width="1705" height="196" alt="image" src="https://github.com/user-attachments/assets/ac23e4e6-73e3-4765-8ec0-1dcea058dc6e" />





















